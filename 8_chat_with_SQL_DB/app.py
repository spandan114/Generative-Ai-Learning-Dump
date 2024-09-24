import streamlit as st
from langchain.agents import create_sql_agent
from pathlib import Path
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

# Load the GROQ API Key
os.environ['HF_TOKEN']=os.getenv("HF_TOKEN")
os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")
groq_api_key=os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="🔎 LangChain - Chat with SQL DB", page_icon="🔎", layout="wide")
st.title("🔎 LangChain - Chat with SQL DB")

LOCALDB = "USE_LOCALDB"
MYSQL = "USE_MYSQL"

radio_opt = ["Use Sqlite 3 - student.db", "Connect to MySQL database"]

selected_opt = st.radio("Select Database", radio_opt)

if radio_opt.index(selected_opt) == 1:
    db_uri = MYSQL
    mysql_host = st.sidebar.text_input("Add MySQL Host")
    mysql_user = st.sidebar.text_input("Use MySQL User")
    mysql_password = st.sidebar.text_input("Use MySQL Password", type="password")
    mysql_database = st.sidebar.text_input("Use MySQL Database")

else:
    db_uri = LOCALDB

if not db_uri:
    st.info("Please enter the database information")

# LLM Model
llm=ChatGroq(groq_api_key=groq_api_key,model_name="Llama3-8b-8192",streaming=True)

@st.cache_resource(ttl="2h")
def configure_db(db_uri,mysql_host=None,mysql_user=None,mysql_password=None,mysql_database=None):
    if db_uri == LOCALDB:
        db_file_path = (Path(__file__).parent / "student.db").absolute()
        print(db_file_path)
        creator = lambda: sqlite3.connect(f"file:{db_file_path}?mode=ro", uri=True)
        return SQLDatabase(create_engine("sqlite://", creator=creator))
    elif db_uri == MYSQL:
        if not mysql_host or not mysql_user or not mysql_password or not mysql_database:
            st.error("Please enter the MySQL database information")
            st.stop()
        else:
            return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_database}"))

if db_uri == MYSQL:
    db = configure_db(db_uri,mysql_host=mysql_host,mysql_user=mysql_user,mysql_password=mysql_password,mysql_database=mysql_database)
else:
    db = configure_db(db_uri)
    st.toast("Using Local Database")

toolkit = SQLDatabaseToolkit(db=db,llm=llm)

agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

if "message" not in st.session_state or st.sidebar.button("Reset"):
    st.session_state.message = []
    st.session_state.message.append({"role": "assistant", "content": "How can i help you ?"})

for msg in st.session_state.message:
    st.chat_message(msg["role"]).write(msg["content"])

user_query = st.chat_input(placeholder="Ask anything from database.")

if user_query:
    st.session_state.message.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)
    
    with st.chat_message("assistant"):
        streamlit_callback=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response=agent_executor.run(st.session_state.message,callbacks=[streamlit_callback])
        st.session_state.message.append({"role": "assistant", "content": response})
        st.write(response)