from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

## Langsmith tracking
# os.environ["LANGCHAIN_TRACKING_V2"]="true"
# os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_TRACING_V2=True
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="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"
LANGCHAIN_PROJECT="default"
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please provide response to the user queries"),
        ("user","Quespip install -U langchain langchain-openaition:{question}")
    ]
)

## streamlit framework
st.title("Langchain demo with Moondream API from open source ollama")
input_text=st.text_input("Search the topic you want")
## open AI LLM call
llm=Ollama(model="moondream")
output_parser=StrOutputParser()
## chain
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))