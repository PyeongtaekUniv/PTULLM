from langchain.text_splitter import RecursiveCharacterTextSplitter
from .loader import pages
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 400,
    chunk_overlap = 20,
    length_function = len,
    is_separator_regex= False,
)
text = text_splitter.split_documents(pages)