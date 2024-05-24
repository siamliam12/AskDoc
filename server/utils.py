from sqlalchemy.orm import Session 
import models,schemas
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores  import FAISS
import pickle
from dotenv import load_dotenv
import os
from langchain_community.llms import OpenAI 
from langchain.chains.question_answering import load_qa_chain
from sentence_transformers import SentenceTransformer
from transformers import pipeline

load_dotenv()
def create_document(db:Session,document:schemas.DocumentCreate):
    db_document = models.Pdf(filename=document.filename,file_location=document.file_location)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document

#this function reads the pdf that is uploaded and breaks that into chunks and stores them.
def read_and_store_document(pdf,query,name):

    if pdf is not None:
        text = ""

        for page in pdf.pages:
            text += page.extract_text()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap = 200,
            length_function = len
        )
        chunks = text_splitter.split_text(text=text)
        print("passed chunks")
        #embeddings
        store_name = name.filename[:-4]
        embedding_location = f"embeddings/{store_name}.pkl"

        if os.path.exists(embedding_location) and os.path.getsize(embedding_location) > 0:
            with open(embedding_location,"rb") as f:
                VectorStore = pickle.load(f)

        else:
            # embeddings = OpenAIEmbeddings()
            # model = SentenceTransformer('all-MiniLM-L6-v2')  # Using a Hugging Face model
            # embeddings = model.encode(chunks)
            embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")# Using a Hugging Face model
            print("passed model")
            VectorStore = FAISS.from_texts(chunks,embedding=embeddings)
            print("VectorStore = FAISS.from_texts(chunks,embedding=embeddings)")
            with open(f"{embedding_location}","wb") as f:
                pickle.dump(VectorStore,f)
        print("passed VectorStore")
        if query:

            # query_embedding = model.encode([query])[0]
            docs = VectorStore.similarity_search(query=query,k=3)
            print("passed docs")
            # llm = OpenAI(model_name='gpt-3.5-turbo')
            # chain = load_qa_chain(llm=llm,chain_type="stuff")
            # response = chain.run(input_documents=docs,question=query)

            qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
            responses = [qa_pipeline(question=query, context=doc.page_content) for doc in docs]
            response_texts = [response['answer'] for response in responses]
            
            return " ".join(response_texts)