

## streamlit
import streamlit as st
st.title("Pyeongtaek Univ. LLM")
st.subheader('평택대학교 LLM', divider='rainbow')
st.write("Team.평택대에 한획을 긋다⭐️ (백승준,김준완,백규현)")
#question = st.text_input("질문을 입력해주세요")


## QA
from answer import return_answer
prompt = st.chat_input("답변 생성")
if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        with st.spinner('로딩 중..'):
            st.write(return_answer(prompt)['result'])

#if st.button("답변 생성"):
#    with st.spinner('로딩 중..'):
#        st.write(return_answer(question)['result'])

#########
# st.write("#PTULLM-V0.1")
########