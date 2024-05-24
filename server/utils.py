from sqlalchemy.orm import Session 
import models,schemas
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores  import FAISS
import pickle
from dotenv import load_dotenv
import os
from langchain_community.llms import OpenAI 
from langchain.chains.question_answering import load_qa_chain

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
        #embeddings
        store_name = name.filename[:-4]
        embedding_location = f"embeddings/{store_name}.pkl"
        if os.path.exists(embedding_location):
            with open(embedding_location,"rb") as f:
                VectorStore = pickle.load(f)
        else:
            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks,embedding=embeddings)
            with open(f"{embedding_location}","wb") as f:
                pickle.dump(VectorStore,f)
        if query:
            docs = VectorStore.similarity_search(query=query,k=3)
            llm = OpenAI(model_name='gpt-3.5-turbo')
            chain = load_qa_chain(llm=llm,chain_type="stuff")
            response = chain.run(input_documents=docs,question=query)
            return response