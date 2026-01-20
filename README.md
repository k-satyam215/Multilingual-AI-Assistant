# Multilingual AI Voice Assistant 🤖🎤

This project is a **voice-enabled AI assistant** built using **Streamlit**, **speech recognition**, and **Google Gemini LLM**.  
It allows users to **ask questions using their voice**, get an **AI-generated response**, and receive the answer as **spoken audio**.

The system demonstrates an **end-to-end speech → AI → speech pipeline**.

---

## 🎯 Objective

The goal of this project is to:
- Build a hands-free AI assistant using voice input
- Convert speech to text for LLM processing
- Generate intelligent responses using a modern LLM
- Convert AI responses back into speech
- Provide an interactive and accessible user experience

---

## 🚀 Key Features

### 🎙️ Voice Input
- Uses microphone input via `speech_recognition`
- Converts spoken language into text
- Handles unrecognized or empty audio gracefully

---

### 🧠 AI-Powered Response
- Uses **Google Gemini (gemini-2.5-flash)** model
- Generates natural language responses
- Handles invalid or empty input safely

---

### 🔊 Text-to-Speech Output
- Converts AI responses into spoken audio using **gTTS**
- Plays audio directly in the Streamlit app
- Allows users to download the generated speech (`speech.mp3`)

---

### 🖥️ Interactive Streamlit UI
- Single-click voice interaction
- Clear loading and error states
- Displays text response alongside audio output

---

## 🧠 How It Works

1. User clicks **“Ask me anything”**
2. Microphone captures user speech
3. Speech is converted to text
4. Text is sent to the Gemini LLM
5. LLM generates a response
6. Response is converted to speech
7. Audio and text are displayed to the user

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **speech_recognition**
- **Google Generative AI (Gemini)**
- **gTTS (Google Text-to-Speech)**
- **python-dotenv**

---



