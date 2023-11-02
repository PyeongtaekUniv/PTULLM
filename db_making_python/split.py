from langchain.text_splitter import RecursiveCharacterTextSplitter
from loader import pages
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 100,
    length_function = len,
    is_separator_regex= False,
)
text = text_splitter.split_documents(pages)