import streamlit as st
from openai import OpenAI

# 🔑 Ambil API key dari secrets
api_key = st.secrets["OPENAI_API_KEY"]

# Inisialisasi client
client = OpenAI(api_key=api_key)

st.title("📂 Upload File Knowledge Base")

# Upload file via Streamlit
uploaded_file = st.file_uploader("Pilih file PDF untuk ditambahkan menjadi knowledge base", type=["pdf"])

if uploaded_file is not None:
    st.write("Nama file:", uploaded_file.name)

    # Upload ke OpenAI vector store
    file_batch = client.vector_stores.file_batches.upload_and_poll(
        vector_store_id="vs_68ae8dab9e20819198991855e92be9da",
        files=[uploaded_file]
    )

    st.success("✅ File berhasil dimasukkan ke vector store!")
    st.json({
        "status": file_batch.status,
        "file_count": file_batch.file_counts
    })
