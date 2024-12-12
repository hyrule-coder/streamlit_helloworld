# streamlit_helloworld

## 概要
「ChatGPT/LangChainによるチャットシステム構築[実践]入門」の6章のアプリケーションの勉強


## 準備
```
python3 -m venv ENV
. ENV/bin/activate
pip install streamlit
pip install langchain langchain-openai langchain-community openai python-dotenv
pip install duckduckgo-search wikipedia
```

## .envファイル
```
OPENAI_API_KEY=[ChatGPTのAPIキー]
OPENAI_API_MODEL=gpt-4o-mini
OPENAI_API_TEMPERATURE=0.5
```

## 実行
```
ENV/bin/streamlit run app.py --server.port 8080
```
