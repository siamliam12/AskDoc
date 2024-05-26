# AskDoc
 Application that allows users to upload PDF documents and ask questions regarding the content of these documents. The backend will process these documents and utilize natural language processing to provide answers to the questions posed by the users.

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