import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_groq import ChatGroq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant please respond to the question asked."),
        ("user","{input}")
    ]
)

def generateResponse(question,model_name,temperature,max_tokens):
    llm=Ollama(model=model_name)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

        
    # Define the Ollama parameters
    params = {
        "input": question,
        "temperature": temperature,  # Controls response creativity (0.0 - 1.0)
        "max_tokens": max_tokens,    # Maximum tokens in the response
        "stop_sequences": ["\n", "\n\n"]  # Optional: stop sequences
    }
    answer = chain.invoke(params)
    return answer


st.title("Q&A Chatbot With OLLAMA")
st.sidebar.title("Settings")
llm = st.sidebar.selectbox("Select an ollama model.",["gemma2:2b"])
temperature = st.sidebar.slider("Select temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Select max tokens", min_value=50, max_value=300, value=50)

st.write("Ask any question to Ollama")
question = st.text_input("question:")

if question:
    answer = generateResponse(question,llm,temperature,max_tokens)
    st.write(answer)
else:
    st.write("Ask any question to OLLAMA")