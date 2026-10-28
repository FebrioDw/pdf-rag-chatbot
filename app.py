import streamlit as st
import os
from dotenv import load_dotenv
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq

load_dotenv()

st.set_page_config(page_title="PDF RAG Chatbot", page_icon="📄")
st.title("🤖 Chatbot Analis Dokumen PDF")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("📂 Menu Dokumen")
    uploaded_file = st.file_uploader("Unggah file PDF di sini", type="pdf")
    if uploaded_file is not None:
        with st.spinner("Memproses..."):
            pdf_reader = PdfReader(uploaded_file)
            raw_text = "".join(page.extract_text() for page in pdf_reader.pages if page.extract_text())
            text_chunks = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100).split_text(raw_text)
            embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
            st.session_state.vector_store = Chroma.from_texts(text_chunks, embedding=embeddings, persist_directory="./document_store")
            st.success("✅ Database siap!")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_question := st.chat_input("Tanyakan sesuatu..."):
    with st.chat_message("user"):
        st.markdown(user_question)
    st.session_state.messages.append({"role": "user", "content": user_question})
    
    with st.chat_message("assistant"):
        if "vector_store" in st.session_state:
            docs = st.session_state.vector_store.similarity_search(user_question, k=3)
            context = "\n\n".join([doc.page_content for doc in docs])
            prompt_text = f"Berdasarkan dokumen berikut, jawab pertanyaan dengan detail. Fokus pada hasil penelitian, temuan ilmiah, atau isi utama jurnal, abaikan bagian profil penulis.\n\nDokumen:\n{context}\n\nPertanyaan: {user_question}"
            
            try:
                # Menggunakan Llama-3 via Groq (Lebih stabil dan sangat cepat)
                llm = ChatGroq(model_name="openai/gpt-oss-120b", temperature=0.3)
                response = llm.invoke(prompt_text)
                st.markdown(response.content)
                st.session_state.messages.append({"role": "assistant", "content": response.content})
            except Exception as e:
                st.error(f"Error sistem: {e}")
        else:
            st.warning("Unggah dokumen PDF dulu.")