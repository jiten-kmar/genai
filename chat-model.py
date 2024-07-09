import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI

#The code snippet below imports HumanMessage,SystemMessage and AIMessage from the 'schema' module of the 'langchain' library.
from langchain.schema import HumanMessage, SystemMessage, AIMessage

load_dotenv()
openapi_key = os.getenv('OPENAI_API_KEY')
#print(f'OPENAI_API_KEY Key: {openapi_key}')

st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")

if 'sessionMessages' not in st.session_state:
    st.session_state['sessionMessages'] = [

        sessionMessages(content="you are a helpful assistent")
    ]


def load_answer(questions):
    st.session_state.sessionMessages


#Initialize the ChatOpenAI object and 
 
chat = ChatOpenAI(temperature=.7, model='gpt-3.5-turbo')

chat.invoke(
    [
        SystemMessage(content="You are a sarcastic AI assistant"),
        HumanMessage(content="Please answer in 30 words: How can I learn driving a car")
    ]
)
