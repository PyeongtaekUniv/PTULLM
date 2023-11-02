from dotenv import load_dotenv
load_dotenv()

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

## streamlit
import streamlit as st
st.title("PTULLM")
st.write("---")

st.header("Pyeongtaek Univ. LLM")
st.write("평택대학교 데이터정보학과")
st.write("Team.평택대에 한획을 긋다⭐️ (백승준,김준완,백규현)")
question = st.text_input("입력해주세요")



## Loader
loader = PyPDFLoader("pturule.pdf")
pages = loader.load_and_split()


## Split
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 400,
    chunk_overlap = 20,
    length_function = len,
    is_separator_regex= False,
)

text = text_splitter.split_documents(pages)

## Embedding Model
from langchain.embeddings import OpenAIEmbeddings
embeddings_model = OpenAIEmbeddings()


## Load it into Chroma
from langchain.vectorstores import Chroma
#db = Chroma.from_documents(text, embeddings_model, persist_directory="./chroma_db")
#chroma_db 만들기

db = Chroma(persist_directory="./chroma_db", embedding_function = embeddings_model)
#이미 만든 chroma_db 사용

## Question Model
from langchain.chat_models import ChatOpenAI
#from langchain.retrievers.multi_query import MultiQueryRetriever
#question = "기숙사 입실 하는 방법을 알려줘"

#llm = ChatOpenAI(temperature=0.05, streaming=True)
#retriever_from_llm = MultiQueryRetriever.from_llm(
#    retriever=db.as_retriever(), llm=llm

# 관련된 문서를 가져오는것
#docs = retriever_from_llm.get_relevant_documents(query=question)
#print(len(docs))
#print(docs)

## QA
from langchain.chains import RetrievalQA

if st.button("답변 생성"):
    with st.spinner('로딩 중..'):
        llm = ChatOpenAI(model_name = 'gpt-3.5-turbo', temperature=0.05, streaming=True)
        qa_chain = RetrievalQA.from_chain_type(llm, retriever=db.as_retriever())
        result = qa_chain({"query":question})
        st.write(result['result'])