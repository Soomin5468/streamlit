import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage
# HumanMessage: 대화형 상황에서 인간 사용자가 입력한 메시지를 나타냄
# SystemMessage: 시스템 또는 모델에서 나온 메시지를 나타내며, 주로 지시사항이나 응답을 설정하는 역할을 함

from langchain_core.output_parsers import StrOutputParser
# StrOutputParser: 모델의 출력값을 받아서 문자열 형식으로 변환하는 파서
# 모델의 응답을 일관성 있게 처리하고 구조화하는 데 유용함

from langchain_core.prompts import ChatPromptTemplate
# ChatPromptTemplate: 모델에게 입력할 프롬프트(지시사항)를 어떻게 구성할지 정의하는 템플릿
# 대화를 위한 지침이나 콘텐츠를 템플릿 형식으로 설정할 수 있게 해줌

from langchain_community.chat_models import ChatOllama
# ChatOllama: Langchain에서 지원하는 Ollama라는 이름의 커뮤니티 기반 챗봇 모델
# 이 모델은 주로 대화 상호작용을 위해 커스터마이즈되었으며, 커뮤니티에서 기여한 최적화된 모델임

st.write("Hello")
st.write("Hello\n")
st.write("Hello\n")

st.write("Hello\n")

st.write("Hello\n")

st.write("Hello\n")
st.write("Hello\n")
st.write("Hello\n")
st.write("Hello\n")
st.write("Hello\n")
st.write("Hello\n")
