import streamlit as st
import pandas as pd


#Armazena no cache para quando houver mudança de página, não ser necessário carregar tudo novamente
@st.cache_data
def carregar_dados():
    tabela = pd.read_excel("Base.xlsx")
    return tabela

base = carregar_dados()

st.title("Hash&Co")
st.write("Bem Vindo, Fernando")
st.table(base.head(10))
