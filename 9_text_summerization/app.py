import validators
import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="🔎 LangChain - Text Summarization", page_icon="🔎", layout="wide")
st.title("🔎 LangChain - Text Summarization")
st.subheader("Text Summarization")

llm=ChatGroq(groq_api_key=groq_api_key,model_name="Llama3-8b-8192")
prompt_template="""
Provide a summary of the following content in 300 words:
Content:{text}

"""
prompt=PromptTemplate(template=prompt_template,input_variables=["text"])


st.sidebar.title("Settings")
url = st.text_input("Enter the url", label_visibility="collapsed")

if st.button("Summarize Yt or website"):
    if not validators.url(url):
        st.error("Please enter a valid url")
    else:
        try:
            with st.spinner("Waiing for response..."):
                if "youtube.com" in url:
                    loader = YoutubeLoader.from_youtube_url(url,add_video_info=True)
                else:
                    loader=UnstructuredURLLoader(urls=[url],ssl_verify=False,
                                                 headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}) 

                documents = loader.load()
                chain = load_summarize_chain(llm=llm,chain_type="stuff",prompt=prompt)
                summary = chain.run(documents)
                st.markdown(summary)
        except Exception as e:
            st.error(e)

