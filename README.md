# FAISS YouTube DataLoader for LangChain LLM Transcript

This repository provides a Python script (`youtube_data_loader.py`) demonstrating the integration of LangChain for processing YouTube video transcripts. The script is designed to extract text content from video transcripts and build a FAISS (Facebook AI Similarity Search) vector store. It utilizes the LangChain library for text processing and vector storage while incorporating multithreading for efficient parallel execution.

## Requirements

- **[LangChain](https://github.com/langchain-ai):** LangChain is a natural language processing library supporting document loading, text extraction, and vector storage.

  ```bash
  pip install langchain
  ```

- **[FAISS](https://github.com/facebookresearch/faiss):** FAISS is a library designed for efficient similarity search and clustering of dense vectors.

  ```bash
  pip install faiss
  ```

- **Additional requirements:** Install other dependencies by executing:

  ```bash
  pip install -r requirements.txt
  ```

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/umangpurwar03/FAISS-Youtube-dataloader-LLM
    ```

2. Navigate to the repository directory:

    ```bash
    cd FAISS-Youtube-dataloader-LLM
    ```

## Usage

1. Modify the `data_dir` variable in `youtube_data_loader.py` to specify the directory containing your YouTube video transcript files.

2. Run the script:

    ```bash
    python youtube_data_loader.py
    ```

    The script concurrently processes each video transcript using multithreading. It loads the data, extracts text content, generates embeddings using Hugging Face models, and stores the vectors in a FAISS vector store.

## Customization

- Customize the embedding model by modifying the `model_name` parameter during the initialization of `HuggingFaceEmbeddings`.

- Adjust the chunk size and overlap in the `RecursiveCharacterTextSplitter` initialization according to specific requirements.

- Feel free to customize other parameters and configurations based on your unique use case.

## Multithreading

The script employs multithreading to concurrently process multiple YouTube video transcripts. The `process_video_transcripts_in_parallel` function initiates a separate thread for each transcript, facilitating efficient parallel processing. Adjust the number of threads based on system capabilities and requirements.

## [URL DataLoader](https://github.com/umangpurwar03/FAISS-URL-dataloader-LLM)

For an Excel data loader, refer to this [link](https://github.com/umangpurwar03/FAISS-URL-dataloader-LLM).

## License

This code is released under the MIT License. Feel free to use and modify it as needed.

## Acknowledgments

- [LangChain](https://github.com/langchain-ai)
- [FAISS](https://github.com/facebookresearch/faiss)

If you find this code helpful or have suggestions for improvement, please feel free to contribute or open an issue.
