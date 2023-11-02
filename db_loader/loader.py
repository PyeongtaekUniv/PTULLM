from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("2023학년도_대학요람.pdf")
pages = loader.load_and_split()