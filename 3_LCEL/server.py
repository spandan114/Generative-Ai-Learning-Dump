import os
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="gemma2-9b-it",groq_api_key=groq_api_key,)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant please respond to the question asked."),
        ("user","{input}")
    ]
)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

app = FastAPI(title="Langchain Server", version="1.0")

add_routes(
    app,
    chain,
    path="/groq",
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)