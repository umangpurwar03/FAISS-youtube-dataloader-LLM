from langchain.document_loaders import YoutubeLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
import threading

# YouTube video URL
video_url = "https://youtu.be/GpgqXCkRO-w?feature=shared"

# Directory to save audio files
faiss_db = 'vectorstore/db_faiss'

def process_transcription(doc):
    # Initialize HuggingFaceEmbeddings using a specific model
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cpu'})
    
    # Create a vector store using FAISS from the transcription and embeddings
    db = FAISS.from_documents(doc, embeddings)
    
    # Save the vector store locally
    db.save_local(os.path.join(faiss_db))
    print("Vector store saved for YouTube video transcription")

def transcribe_youtube_video():
    # Ensure the directory exists
    if not os.path.exists(faiss_db):
        os.makedirs(faiss_db)  # Corrected variable name from 'save_dir' to 'faiss_db'
        print(f"Created directory: {faiss_db}")

    # Load content from YouTube video using YoutubeLoader
    loader = YoutubeLoader.from_youtube_url(video_url, add_video_info=True)  # Corrected method name to 'from_url'
    doc = loader.load()
    print("Transcription completed for the YouTube video")

    # Initialize a text splitter to divide documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = text_splitter.split_documents(doc)
    print(texts)
    print(f"Texts splitted")

    # Process transcription
    process_transcription(texts)

if __name__ == "__main__":
    transcribe_youtube_video()
