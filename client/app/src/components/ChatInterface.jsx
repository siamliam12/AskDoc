import  { useState } from 'react';
import styled from 'styled-components';
import LoadingSpinner from './Spinner'; 

const ChatContainer = styled.div`
  display: flex;
  flex-direction: column;
  height: 80vh;
  width: 100%;
  max-width: 800px;
  margin: auto;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
`;

const ChatHeader = styled.div`
  padding: 16px;
  background-color: #007bff;
  color: white;
  text-align: center;
  font-size: 24px;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
`;

const ChatHistory = styled.div`
  flex: 1;
  padding: 16px;
  overflow-y: auto;
  background-color: #f7f7f7;
  display: flex;
  flex-direction: column;
`;

const ChatMessage = styled.div`
  margin-bottom: 12px;
  padding: 12px 18px;
  background-color: ${(props) => (props.isUser ? '#007bff' : '#e5e5ea')};
  color: ${(props) => (props.isUser ? 'white' : 'black')};
  align-self: ${(props) => (props.isUser ? 'flex-end' : 'flex-start')};
  border-radius: 20px;
  max-width: 75%;
  word-wrap: break-word;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
`;

const ChatInputContainer = styled.div`
  display: flex;
  padding: 16px;
  border-top: 1px solid #ddd;
  background-color: white;
`;

const ChatInput = styled.input`
  flex: 1;
  padding: 12px 20px;
  border: 1px solid #ddd;
  border-radius: 20px;
  font-size: 16px;
  outline: none;
`;

const SendButton = styled.button`
  margin-left: 8px;
  padding: 12px 20px;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 20px;
  cursor: pointer;
  font-size: 16px;
  outline: none;
  transition: background-color 0.3s ease-in-out;

  &:hover {
    background-color: #0056b3;
  }
`;

const ChatInterface = ({ pdfId }) => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false); // Add loading state
  const handleSend = async () => {
    if (input.trim()) {
      const userMessage = { text: input, isUser: true };
      setMessages((prevMessages) => [...prevMessages, userMessage]);
      setLoading(true); // Set loading to true
      try {
        // Send the question to the backend with pdfId
        const questionResponse = await fetch('http://127.0.0.1:8000/questions', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ question: input, pdf_id: String(pdfId) }), // Convert pdfId to string
        });

        if (questionResponse.ok) {
          const questionData = await questionResponse.json();
          const questionId = questionData.data;
          console.log(questionId)

          // Get the answer from the backend using pdfId and questionId
          const answerResponse = await fetch(`http://127.0.0.1:8000/answer/${pdfId}/${questionId}`);

          if (answerResponse.ok) {
            const answerData = await answerResponse.json();
            console.log(answerData)
            const answerMessage = { text: answerData.Answer, isUser: false };
            setMessages((prevMessages) => [...prevMessages, userMessage, answerMessage]);
          } else {
            console.error('Error fetching answer:', answerResponse.statusText);
          }
        } else {
          const errorData = await questionResponse.json();
          console.error('Error submitting question:', questionResponse.statusText, errorData);
        }
      } catch (error) {
        console.error('Error:', error);
      }
      setLoading(false); // Set loading to false
      setInput('');
    }
  };

  return (
    <ChatContainer>
      <ChatHeader>Chat Interface</ChatHeader>
      <ChatHistory>
        {messages.map((msg, index) => (
          <ChatMessage key={index} isUser={msg.isUser}>
            {msg.text}
          </ChatMessage>
        ))}
      {loading && <LoadingSpinner />}
      </ChatHistory>
      <ChatInputContainer>
        <ChatInput
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..."
        />
        <SendButton onClick={handleSend}>Send</SendButton>
      </ChatInputContainer>
    </ChatContainer>
  );
};

export default ChatInterface;
