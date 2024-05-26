# AskDoc
 Application that allows users to upload PDF documents and ask questions regarding the content of these documents. The backend will process these documents and utilize natural language processing to provide answers to the questions posed by the users.

# Software Architecture 

#### Overview

The application enables users to upload PDF documents and ask questions about their content. The backend, built with FastAPI, processes these documents using LangChain for natural language processing and a Hugging Face model to provide answers to the users' questions. The architecture includes endpoints for uploading PDFs, submitting questions, and processing documents to create and store vector embeddings locally.

#### Architecture Components

1. **Frontend**
   - **User Interface**: Web-based interface for users to upload PDFs and ask questions.
   - **File Upload Form**: Allows users to select and upload PDF files.
   - **Question Submission Form**: Allows users to input questions related to the uploaded PDFs.
   - **Response Display**: Displays the answers provided by the backend.

2. **Backend**
   - **Framework**: FastAPI for creating API endpoints and handling HTTP requests.
   - **NLP Processing**: LangChain for processing and managing language tasks.
   - **Model Integration**: Hugging Face models for generating responses to user questions.
   - **Storage**: Local file system for storing PDFs and vector embeddings.

3. **Endpoints**
   - **PDF Upload Endpoint** (`/upload-pdf`): Accepts PDF files and saves them locally.
   - **Question Submission Endpoint** (`/question`): Accepts user questions related to the uploaded PDFs.
   - **Document Processing Endpoint** (`/answer`): Processes the uploaded PDF, extracts text, creates vector embeddings, and stores them locally.

#### Detailed Architecture

1. **Frontend**
   - **ReactJs**: web technologies for creating the user interface.
   - **File Upload Component**: A form with file input to allow PDF uploads.
   - **Question Input Component**: A form for users to submit questions like a chatapp.
   - **Answer Display Component**: Displays the answers retrieved from the backend.

2. **Backend (FastAPI)**
   - **Endpoints**:
     - **Upload PDF (`/upload-pdf`)**:
       - Method: `POST`
       - Function: Accepts PDF file upload, saves the file to a local directory.
     - **Submit Question (`/question`)**:
       - Method: `POST`
       - Function: Accepts questions from the user, retrieves the relevant document, processes it, and returns the answer.
     - **Process Document (`/answer`)**:
       - Method: `POST`
       - Function: Reads the uploaded PDF, extracts text, breaks it into chunks, embeds the text using LangChain, and stores the embeddings locally.

3. **Processing Workflow**
   - **PDF Upload**:
     - User uploads a PDF via the frontend.
     - The file is sent to the `/upload-pdf` endpoint and saved locally.
   - **Document Processing**:
     - Triggered by the `/answer` endpoint.
     - Reads the PDF from the local storage.
     - Extracts text and processes it into chunks.
     - Uses LangChain to create embeddings of these chunks.
     - Stores the embeddings in a local vector store.
   - **Question Answering**:
     - User submits a question via the frontend.
     - The question is sent to the `/question` endpoint.
     - The backend retrieves the relevant document embeddings.
     - LangChain processes the question and retrieves relevant text chunks.
     - Hugging Face model generates an answer based on the retrieved text.
     - The answer is returned to the frontend and displayed to the user.

4. **Storage**
   - **Local File Storage**:
     - PDFs are stored in a specific directory.
     - Vector embeddings are stored in a local vector store.

#### Technologies Used

- **FastAPI**: Framework for building API endpoints.
- **Reactjs**: Framework for building Web UI.
- **LangChain**: For text processing, chunking, and creating embeddings.
- **Hugging Face**: For utilizing pre-trained NLP models to generate answers.
- **Local Storage**: For saving PDFs and vector embeddings.

## Installation and Setup
 In order to run the application in your local system you have to install dependencies and then it should run smoothly.
 ### Step 1 : Clone the repository
 First clone the repository from github to your local repository
 ```git clone https://github.com/siamliam12/AskDoc.git```
# System Requirements:
 Python and nodejs should be installed
# Backend Setup : installing backend dependencies
 Go to the folder AskDoc and then into the server folder
 ``` cd AskDoc
     cd server
```
 now create a virtual environment in python
 ``` python -m venv env```

after that install all the packages
```pip install -r requirements.txt```

that should do the backend part.

# Frontend Setup: installing backend dependencies
 Go to the folder AskDoc and then into the Client folder
 ``` cd AskDoc
     cd client
```
now install the dependencies using npm
``` npm i```

that should do the Frontend part.

## Running the Application
in order to run the app we need two terminals. one for the client and one for the server
in the client folder open a terminal and run the server
``` npm run dev```
in the server folder open a terminal and run the server
``` uvicorn main:app --reload```

after this it will take some time to run the file but the application should be running on your local machine.