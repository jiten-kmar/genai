!pip3 install --upgrade langchain langchain-openai
!pip3 install --upgrade  openai
!pip3 install huggingface-hub==0.23.4 langchain-community

from langchain_openai import OpenAI
from langchain.llms import HuggingFaceEndpoint
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


import os
os.environ["OPENAI_API_KEY"]="<key>"
os.environ["HUGGINGFACEHUB_API_TOKEN"]="<key>"


llm=OpenAI(model_name="gpt-3.5-turbo-instruct")
llm=HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2" # Model link : https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2
)

our_query="what is the capital of  United states"
completion=llm.invoke(our_query)

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
embeddings = embed_model.get_text_embedding("Hello World!")
print(len(embeddings))
print(embeddings[:5])



