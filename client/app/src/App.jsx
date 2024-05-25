import { useState } from 'react';
import Navbar from './components/Navbar';
import './App.css'
import PdfUploadComponent from './components/Upload';
import ChatInterface from './components/ChatInterface';

function App() {
  const [isPdfUploaded, setIsPdfUploaded] = useState(false);
  const [pdfId, setPdfId] = useState(null);

  const handleFileUpload = async (file) => {
    console.log('Uploaded file:', file);
    const formdata = new FormData();
    formdata.append('file', file);
    try{
      const response = await fetch("http://127.0.0.1:8000/upload-doc",{
        method: 'POST',
        body: formdata,
      })
      if (response.ok){
        const data =  await response.json()
        console.log("File uploaded successfully",data)
        setPdfId(data.id);
        setIsPdfUploaded(true);
      }
      else{
        console.log("Error uploading file:", response.statusText)
      }
    }catch(error){
      console.error('Error uploading file:', error);
    }
  };

  return (
    <>
    <div>
    <Navbar/>
    {isPdfUploaded ? (
        <ChatInterface pdfId={pdfId}/>
      ) : (
        <PdfUploadComponent onFileUpload={handleFileUpload} />
      )}
    </div>
    </>
  )
}

export default App
