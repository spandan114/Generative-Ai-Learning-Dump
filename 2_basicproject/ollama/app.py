import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Langsmith track
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant please respond to the question asked."),
        ("user","Question: {input}")
    ]
)

st.title("Langchain Demo With GEMMA 2B")
input_text = st.text_input("What question in your mind?")

# LLAMA3.1
llama = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()
chain = prompt | llama | output_parser

if input_text:
    st.write(chain.invoke(input=input_text))