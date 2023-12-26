import streamlit as st
from streamlit import session_state
from utils.driver_code_summarization import summarizer

if 'text_summary' not in session_state:
    session_state['text_summary']= ""

def summarize(input_text):
    summarized_text= session_state['text_summary']= summarizer(input_text)[0]['summary_text']
    session_state['text_summary'] = summarized_text

st.title("Text Summarization")

input_text= st.text_area(label= "Please paste the long text here", 
              placeholder="paste here")

st.text_area("Summary", value=session_state['text_summary'])

st.button("Summarize", on_click=summarize, args=[input_text])

