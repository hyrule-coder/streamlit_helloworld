import os

import streamlit as st
from dotenv import load_dotenv
from langchain_openai.chat_models.base import ChatOpenAI
from langchain_core.messages.human import HumanMessage

load_dotenv()

st.title("langchain-streamlit-app")

if "messages" not in st.session_state: # st.session_stateに"messages"がない場合、空のリストを作成
    st.session_state.messages = []

for message in st.session_state.messages: # st.session_state.messagesに格納されているメッセージを表示
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("What's up?")

if prompt:
    # st.session_state.messagesにユーザーの入力を追加
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        chat = ChatOpenAI(
            model=os.environ["OPENAI_API_MODEL"],
            temperature=os.environ["OPENAI_API_TEMPERATURE"],
        )
        messages = [HumanMessage(content=prompt)]
        response = chat(messages)
        st.markdown(response.content)

    # st.session_state.messagesにアシスタントの返答を追加
    st.session_state.messages.append({"role": "assistant", "content": response.content})
    