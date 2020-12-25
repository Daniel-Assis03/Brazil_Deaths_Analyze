import pandas as pd
import numpy as np
import streamlit as st

@st.cache
def get_data():
    return pd.read_csv(r'C:\Users\User\Desktop\ADS\Datasets\Brazil Deaths\death_cause_brazil.csv')
pass

data = get_data()

def By_sex():
    data = get_data()
    data_genres = data.groupby(by='gender').size().sort_values(ascending=False)
    return data_genres
pass
    
def By_state():
    data = get_data()
    data_states = data.groupby(by='state').size().sort_values(ascending=False)
    return data_states
pass
   
def By_color():
    data = get_data()
    data_colors = data.groupby(by='color').size().sort_values(ascending=False)
    return data_colors
pass



st.title("Dados das mortes no Brasil com base na cor da pele, sexo e Estado")
st.markdown("Inclui idade, causa e data da morte")
st.markdown("Fonte: https://www.kaggle.com/amandalk/cause-of-death-in-brazil-20192020")

btn_state = st.button("Total de mortes por Estado")

btn_genre = st.button("Total de mortes por Sexo")

btn_color = st.button("Total de mortes por cor/etnia")


if btn_state:
    st.subheader("Total de mortes por estados")
    total_mortes_uf = By_state()
    st.write(total_mortes_uf)
pass

if btn_genre:
    st.subheader("Total de Mortes por genero \n" " F = Feminino \n M = Masculino")
    total_mortes_sex = By_sex()
    st.write(total_mortes_sex)
pass

if btn_color:
    st.subheader("Total de mortes por Cor/Etnia")
    total_mortes_color = By_color()
    st.write(total_mortes_color)
pass



st.sidebar.title("Pesquisar")

pesquisa_cor = st.sidebar.radio("Cor", data.color.unique())
pesquisa_sexo = st.sidebar.radio("Sexo", data.gender.unique())
pesquisa_state = st.sidebar.text_input("Digite a SIGLA do estado")
btn_busca = st.sidebar.button("Buscar dados combinados")

def search():
   resultado_busca = data.loc[(data.gender==pesquisa_sexo)&(data.state==pesquisa_state)&(data.color==pesquisa_cor)]
   return resultado_busca
pass

if btn_busca:
    busca = search()
    total = len(search())
    st.subheader("Resultados Encontrados")
    st.write(total)
    st.write(busca)
pass

