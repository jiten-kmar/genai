import streamlit as st
from langchain_openai import OpenAI
from langchain.llms import HuggingFaceEndpoint
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


import os
os.environ["HUGGINGFACEHUB_API_TOKEN"]="<token>"
repos_id="mistralai/Mistral-7B-Instruct-v0.2"



def load_answer(question):
    llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2", temperature=0.5,huggingfacehub_api_token="<token>")
    answer=llm.invoke(question)
    return answer

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")


#App UI starts here
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")

def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text


user_input=get_text()
#response = load_answer(user_input)

submit = st.button('Generate')  

#If generate button is clicked
if submit:
    response = load_answer(user_input)
    st.subheader("Answer:")
    st.write(response)
    embeddings = embed_model.get_text_embedding(user_input)
    st.write(len(embeddings))
    st.write(embeddings[:5])
