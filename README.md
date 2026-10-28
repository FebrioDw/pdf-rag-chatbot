# 📄 RAG PDF Chatbot dengan LangChain & Groq API

Aplikasi *chatbot* berbasis Retrieval-Augmented Generation (RAG) yang dirancang untuk mengekstraksi dan menganalisis informasi dari dokumen PDF. Proyek ini mengintegrasikan Large Language Model (LLM) melalui Groq API untuk menghasilkan pemrosesan teks yang efisien dan akurat.

## 🚀 Fitur Utama
* Ekstraksi dan pemrosesan teks PDF yang berjalan secara lokal.
* Penyimpanan dan pencarian vektor menggunakan arsitektur ChromaDB dan HuggingFace Embeddings.
* Integrasi inferensi bahasa alami berkinerja tinggi menggunakan Groq API.
* Arsitektur modular yang memungkinkan pergantian model LLM dengan konfigurasi minimal.

## 🛠️ Cara Instalasi
1. *Clone* repositori ini.
2. Buat *virtual environment* dan jalankan: `pip install -r requirements.txt`
3. Buat file `.env` dan masukkan API Key: `GROQ_API_KEY="sandi_milikmu"`
4. Jalankan aplikasi: `streamlit run app.py`

## 🧠 Konfigurasi Model AI

Sistem ini didesain secara modular. Pengguna dapat mengubah model LLM yang digunakan dengan menyesuaikan parameter pada file `app.py`:

```python
# Sesuaikan nama model dengan ID yang tersedia di ekosistem Groq
llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.3)
