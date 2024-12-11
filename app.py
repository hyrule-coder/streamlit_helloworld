import streamlit as st

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
        response = "こんにちは"
        st.markdown(response)

    # st.session_state.messagesにアシスタントの返答を追加
    st.session_state.messages.append({"role": "assistant", "content": response})
    