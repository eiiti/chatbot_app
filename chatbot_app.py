import os
import openai
import streamlit as st

# APIキーを設定
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(message):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response_text = response.choices[0].text.strip()
    return response_text

st.title('GPTチャットボット')

user_message = st.text_input("あなたのメッセージ:")

if st.button('送信'):
    response = generate_response(user_message)
    st.write(f"チャットボット: {response}")
