from dotenv import load_dotenv
load_dotenv()

from langchain.vectorstores import Chroma
from embedding import embeddings_model
from split import text

# making db
db = Chroma.from_documents(text, embeddings_model, persist_directory="../chroma_db")
### If you want to embed a PDF, you need to change it at loader.py