// PdfUploadComponent.js
import { useDropzone } from 'react-dropzone';
import styled from 'styled-components';

const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f8f9fa;
`;

const DropzoneContainer = styled.div`
  border: 2px dashed #6c757d;
  border-radius: 12px;
  width: 50%;
  max-width: 600px;
  padding: 60px;
  text-align: center;
  background-color: #ffffff;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: border-color 0.3s ease-in-out, box-shadow 0.3s ease-in-out;

  &:hover {
    border-color: #007bff;
    box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
  }

  p {
    font-size: 18px;
    color: #6c757d;
    margin: 0;
  }
`;

const UploadButton = styled.button`
  margin-top: 20px;
  padding: 12px 24px;
  font-size: 16px;
  color: #ffffff;
  background-color: #007bff;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out, transform 0.3s ease-in-out;

  &:hover {
    background-color: #0056b3;
    transform: scale(1.05);
  }
`;

const PdfUploadComponent = ({ onFileUpload }) => {
  const { getRootProps, getInputProps } = useDropzone({
    accept: 'application/pdf',
    onDrop: acceptedFiles => {
      onFileUpload(acceptedFiles[0]);
    },
  });

  return (
    <Container>
      <DropzoneContainer {...getRootProps()}>
        <input {...getInputProps()} />
        <p>Drag & drop a PDF file here, or click to select a file</p>
        <UploadButton type="button">Upload a PDF</UploadButton>
      </DropzoneContainer>
    </Container>
  );
};

export default PdfUploadComponent;
