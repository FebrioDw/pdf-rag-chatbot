# 📄 RAG PDF Chatbot dengan LangChain & Groq API

Aplikasi *chatbot* berbasis Retrieval-Augmented Generation (RAG) untuk menganalisis dokumen PDF secara cerdas menggunakan ekosistem Llama 3 / Mixtral via Groq API yang super cepat.

## 🚀 Fitur Utama
* Ekstraksi dokumen PDF secara lokal.
* Pencarian vektor menggunakan arsitektur ChromaDB & HuggingFace.
* Pemrosesan bahasa alami menggunakan Groq API.
* Modular LLM: Bebas ganti model AI kapan saja.

## 🛠️ Cara Instalasi
1. *Clone* repositori ini.
2. Buat *virtual environment* dan jalankan: `pip install -r requirements.txt`
3. Buat file `.env` dan masukkan API Key kamu: `GROQ_API_KEY="sandi_milikmu"`
4. Jalankan aplikasi: `streamlit run app.py`

## 🧠 Cara Mengganti Model AI
Proyek ini bersifat modular. Kamu bisa mengganti model LLM yang digunakan dengan mengedit satu baris di `app.py`:
```python
# Ganti nama model sesuai dengan ID di Groq Playground
llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.3)