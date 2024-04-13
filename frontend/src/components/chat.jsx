import React, { useState } from 'react';
import ChatMessages from './chat.messages';
import {sendMessage} from '../services/chat.service';


function Chat(props) {
    const [messages, setMessages] = useState([]);
    const [message, setMessage] = useState('');

    const handleChange = (e) => {
        setMessage(e.target.value);
      };
    
    const handleSubmit = (e) => {
        e.preventDefault();
        if (message.trim() !== '') {
        send(message);
        setMessage('');
        }
    };
    const send = (message)=>{
        sendMessage({message, history:messages}).then(result=>{if (result) setMessages(result)})
    }


    return (
      <div className="chat">
        Chat
        <form onSubmit={handleSubmit}>
            <input
            type="text"
            value={message}
            onChange={handleChange}
            placeholder="Type your message..."
            className="chat-input"
            />
            <button type="submit" className="send-button">
            Send
            </button>
        </form>
        <ChatMessages messages={messages}/>
      </div>
    );
  }

export default Chat;
