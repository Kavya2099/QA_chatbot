#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
from langchain.chat_models import AzureChatOpenAI


## Function to load OpenAI model and get respones

def get_openai_response(question):
    azure_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
    azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

    llm = AzureChatOpenAI(
    openai_api_version=os.getenv("OPENAI_API_VERSION"),
    azure_deployment="gpt-35-turbo",
    )
    response=llm.invoke(question)
    
    
    return response.content


## initialize streamlit app

st.set_page_config(page_title="Q&A bot")

st.header("Langchain Application")

input=st.text_input("Input: ",key="input")
response= get_openai_response(input)

submit= st.button("Ask the question")


if submit:
    st.subheader("The response is")
    st.write(response)
