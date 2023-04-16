import os
import openai
import streamlit as st

# OpenAI APIキーを設定
openai.api_key = os.getenv("OPENAI_API_KEY")

# メッセージを入力してGPTからの応答を生成する関数
def generate_response(message):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"User: {message}\nChatbot:",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response_text = response.choices[0].text.strip()
    return response_text

# タイトルを設定
st.title('GPTチャットボット')

# ユーザーからのメッセージを受け取るテキストボックスを作成
user_message = st.text_input("あなたのメッセージ:")

# 送信ボタンがクリックされたら、GPTからの応答を表示
if st.button('送信'):
    response = generate_response(user_message)
    st.write(f"チャットボット: {response}")
