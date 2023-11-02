#from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader

loader = DirectoryLoader('../data2', glob = "*.txt", loader_cls=TextLoader)

pages = loader.load()