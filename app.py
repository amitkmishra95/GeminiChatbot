import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(
    page_title="Gemini ChatBot",
    page_icon=":speech_balloon:",
   #page_icon=":alien:", 
    layout="centered",  
)

#AIzaSyDIya16Vsts7Lep1mFI
genai.configure(api_key="AIzaSyDSxWZwBWei9FENO6JivrMvQnobM--7DrA")
model = genai.GenerativeModel('gemini-pro')


def role_to_streamlit(role):
  if role == "model":
    return "assistant"
  else:
    return role


if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history = [])


st.title("Chat with Bot..")


for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)


if prompt := st.chat_input("How may I help you?"):
    st.chat_message("user").markdown(prompt)
    
    response = st.session_state.chat.send_message(prompt) 
    
 
    with st.chat_message("assistant"):
        st.markdown(response.text)


st.markdown("""
            
    <style>
        /* Style for the header */
        .stApp {
            background-color: #E4F5E8;
        }
            .header{
            color:#F70A0C;
            }

           .stChatbot .stMessage {
            background-color: red; /* Set the background color to red */
            color: white; /* Change text color to white for contrast */
            border-radius: 10px; /* Round corners for the chat bubble */
            padding: 10px; /* Add padding inside the message bubble */
        }
        
        /* You can also target the chatbot's input box if needed */
        .stChatbot .stTextInput>div>input {
            background-color: #f7f7f7; /* Light background for input field */
            color: #333; /* Dark text for input field */
            border: 2px solid #ccc; /* Light border */
            padding: 10px; /* Padding inside input box */
            border-radius: 5px; /* Rounded corners for input box */
        }

        .stChatbot .stTextInput>div>input:focus {
            border-color: red; /* Focus color for the input field */
        }        
        h1 {
            color: red;
            font-family: 'Arial', sans-serif;
            text-align: left;
        }

        /* Customizing the button style */
        .stButton>button {
            background-color: red;
            color: white;
            font-size: 16px;
            padding: 12px 24px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
        }

        .stButton>button:hover {
            background-color: #0A15F7 ;
        }

        /* Styling for the sidebar */
        .css-1d391kg {
            background-color: #0A15F7;
        }

        /* Customizing markdown text */
        .markdown-text {
            color: #E4080A;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)



