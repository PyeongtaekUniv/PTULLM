from langchain.vectorstores import Chroma
from .embedding import embeddings_model

load_db = Chroma(persist_directory="./chroma_db", embedding_function = embeddings_model)