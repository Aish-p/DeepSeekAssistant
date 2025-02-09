# 🧠 DeepThink: Your Smart, Local AI Chatbot

DeepThink is a locally running AI chatbot built using DeepSeek Intelligence and Streamlit. This project showcases real-time reasoning, multi-chat support, and an intuitive interface—all running without internet or API keys.


## 🎯 Features  

* **Real-Time AI Chat** – Chat with DeepThink using DeepSeek's deep-learning-powered responses.

* **Multi-Chat Support** – Create, rename, and delete chats across multiple chat sessions without losing session history.

* **Smart Thinking Phase** – AI first "thinks" before responding, mimicking human-like reasoning.

* **Runs 100% Locally** – No internet, no API keys—your data stays private.


## 🔧 Setup Guide

1️⃣ **Install & Run Ollama**
Ensure that you have Ollama installed and running. Download it from 🔗 [here](https://ollama.com/download)

2️⃣ **Pull the DeepSeek-R1 Model**
After installing Ollama, run the following command in your terminal:
  ```
  ollama pull deepseek-r1
  ```

3️⃣ **Install Dependencies**
  ```
  pip install -r requirements.txt
  ```

4️⃣ **Run the Chatbot** 🚀

Start the Streamlit app by running:
  ```
  streamlit run app.py
  ```


## 🖥️ Usage Guide

* **Start a New Chat:** Click **"➕ New Chat"** in the sidebar to begin.
* **Chat with DeepThink:** Type your message and hit **Enter**—AI will respond dynamically.
* **Rename Chats:** Click the ✏️ **Rename** button to customize chat titles.
* **Delete Chats:** Click 🗑️ **Delete** to remove unwanted conversations.
* **Switch Between Chats:** Click any chat title in the sidebar to revisit old conversations.


## 📷 UI Preview

<div align="center">
  <p><strong>Chat Interface</strong></p>
  <img src="/assets/chat_interface.PNG" alt="Chat Interface" width="700">
</div>
<br>

<div align="center">
  <p><strong>Thinking Mode</strong></p>
  <img src="/assets/thinking_mode.PNG" alt="Thinking Mode" width="700">
</div>
<br>

<div align="center">
  <p><strong>Response</strong></p>
  <img src="/assets/response.PNG" alt="Response" width="700">
</div>
<br>

<div align="center">
  <p><strong>Rename</strong></p>
  <img src="/assets/rename.PNG" alt="Rename" width="700">
</div>
<br>

<div align="center">
  <p><strong>Renamed</strong></p>
  <img src="/assets/renamed.PNG" alt="Renamed" width="700">
</div>
<br>

<div align="center">
  <p><strong>Delete</strong></p>
  <img src="/assets/delete.PNG" alt="Delete" width="700">
</div>
<br>

<div align="center">
  <p><strong>Deleted</strong></p>
  <img src="/assets/deleted.PNG" alt="Deleted" width="700">
</div>
<br>

## 🏗️ Tech Stack

| Technology      | Purpose              |
|---------------|----------------------|
| **Python** 🐍  | Backend Logic        |
| **Streamlit** 🎨 | Interactive UI       |
| **DeepSeek** 🧠  | AI Chat Model        |
| **Regex & Base64** 🔤 | Message Formatting  |
