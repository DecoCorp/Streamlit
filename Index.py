# Importando as libs
import streamlit as st
import os
import pandas as pd
import plotly.express as px
from PIL import Image

# Configurar o layout da página
st.set_page_config(layout="wide")

def highlight_missing_data(val):
    return 'background-color: #ffcccc' if pd.isnull(val) else ''

# Criando o sidebar
def sidebar():
    sidebar = st.sidebar
    # logo + data
    logo = "D:/Códigos/Dash/img/tv_bahia_BRANCA.png"
    Logo_Ba = Image.open(logo)
    st.sidebar.image(Logo_Ba, use_column_width=True)
    st.sidebar.markdown("<h3 style='text-align: center;'>Relatórios</h3>", unsafe_allow_html=True)
    sidebar.write('---')
    st.sidebar.markdown("<h3 style='text-align: center;'>Maio/2023</h3>", unsafe_allow_html=True)
    # botoes Ranking + Historicos (Mensal, Anual e Min a min)
    st.sidebar.button('RANKING PNT', key='#Pnt')
    st.sidebar.button('HISTÓRICO MENSAL', key='Mensal')
    st.sidebar.button('HISTÓRICO ANUAL', key='Anual')
    st.sidebar.button('MINUTO A MINUTO', key='MinMin')
    
# Criando as defs dos graficos
def GraficoRanking():
    # Ranking PNT - 07 Às 24h
    st.markdown("<h1 style='text-align: center;'>RANKING PNT - 07 ÀS 24H</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        dados_tabela = {'Mês - Rat': ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL','MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO'],
                        '2021': [12, 9, 8, 7, 6, 7, 8, 8, 8, 9, 7, 7,],
                        '2022': [12, 9, 8, 7, 6, 7, 8, 8, 8, 9, 7, 7,],                       
                        '2023': [12, 9, 8, 7, 0, 0, 0, 0, 0, 0, 0, 0,]}
        df_tabela = pd.DataFrame(dados_tabela)
        st.table(df_tabela)
    with col2:
        dados_tabela = {'Mês - Rat': ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL','MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO'],
                        '2021': [12, 9, 8, 7, 6, 7, 8, 8, 8, 9, 7, 7,],
                        '2022': [12, 9, 8, 7, 6, 7, 8, 8, 8, 9, 7, 7,],                       
                        '2023': [12, 9, 8, 7, 0, 0, 0, 0, 0, 0, 0, 0,]}
        df_tabela = pd.DataFrame(dados_tabela)
        st.table(df_tabela)
        
    # Historico Mensal (Audiência x share)
def HistMensal():
    st.markdown("<h1 style='text-align: center;'>HISTÓRICO MENSAL</h1>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns(5)  # Criar cinco colunas
    with col1:
        st.write("")  # Espaço em branco à esquerda
        btn1 = st.button("06h às 12h")
    with col2:
        st.write("")  # Espaço em branco à direita
        st.button("07h às 24h")
    with col3:
        st.write("")  # Espaço em branco à esquerda
        st.button("12h às 18h")
    with col4:
        st.write("")  # Espaço em branco à direita
        st.button("18h às 24h")
    with col5:
        st.write("")  # Espaço em branco à direita
        st.button("24h às 30h")
        
    dadosHistMensal = pd.read_csv('dados/historico_mensal_preparado_0612_2023_5.csv')
    dfHistMensal = pd.DataFrame(dadosHistMensal)

    col1, col2 = st.columns(2)
    # 06h às 12h
    with col1:
        st.title("Audiência")
        if 'Emissora' in dfHistMensal and 'Rat' in dfHistMensal and 'Data' in dfHistMensal:
            st.write("Histórico Mensal - Audiência - 06h às 12h")

            fig = px.line(dfHistMensal, x='Data', y='Rat', color='Emissora', labels={'Rat': 'Índice'}, markers=True)

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("As colunas 'Emissora', 'Rat' ou 'Data' não estão presentes no DataFrame.")
    with col2:
        st.title('Share')
        if 'Emissora' in dfHistMensal and 'Shr' in dfHistMensal and 'Data' in dfHistMensal:
            st.write("Histórico Mensal - Share - 06h às 12h")

            fig = px.line(dfHistMensal, x='Data', y='Shr', color='Emissora', labels={'Shr': 'Índice'})

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("As colunas 'Emissora', 'Shr' ou 'Data' não estão presentes no DataFrame.")
        
        # 07h às 24h
        
        # 12h às 18h
        # 18h às 24h
        # 24h às 30h
        
    # Historico Anual (Audiência x share)
def HistAnual():
    st.markdown("<h1 style='text-align: center;'>HISTÓRICO ANUAL</h1>", unsafe_allow_html=True)
    
    DadosHistAnual = pd.read_csv('dados/historico_anual_preparado_5.csv')
    dfHistAnual = pd.DataFrame(DadosHistAnual)
    
    col1, col2 = st.columns(2)  # Criar duas colunas
    with col1:
        st.title("Audiência")
        if 'Emissoras' in dfHistAnual and 'Rat' in dfHistAnual and 'Datas' in dfHistAnual:
            st.markdown("<h5 style='text-align: center;'>Gráfico Histórico Anual - Audiência</h5>", unsafe_allow_html=True)

            fig = px.line(dfHistAnual, x='Datas', y='Rat', color='Emissoras', labels={'Rat': 'Índice'}, markers=True)

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("As colunas 'Emissoras', 'Rat' ou 'Datas' não estão presentes no DataFrame.")
    with col2:
        st.title("Share")
        if 'Emissoras' in dfHistAnual and 'Shr' in dfHistAnual and 'Datas' in dfHistAnual:
            st.markdown("<h5 style='text-align: center;'>Gráfico Histórico Anual - Share</h5>", unsafe_allow_html=True)

            fig = px.line(dfHistAnual, x='Datas', y='Shr', color='Emissoras', labels={'Shr': 'Índice'}, markers=True)

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("As colunas 'Emissoras', 'Shr' ou 'Datas' não estão presentes no DataFrame.")


    # Historico min a min dia completo (audiência x share)
def HistMinXMin():
    #Segunda
    st.markdown("<h1 style='text-align: center;'>MINUTO A MINUTO DIA COMPLETO</h1>", unsafe_allow_html=True)
    
    DadosMinXMin = pd.read_csv('dados/minuto_minuto_preparado_ss_5.csv')
    dfMinxMin = pd.DataFrame(DadosMinXMin)
    
    col1, col2 = st.columns(2)  # Criar duas colunas
    with col1:
        st.title("Audiência")
        if 'Hora' in dfMinxMin and 'Rat' in dfMinxMin and 'Data' in dfMinxMin:

            # Use 'Data' para definir as cores ou marcadores para cada mês
            fig = px.scatter(dfMinxMin, x='Hora', y='Rat', color='Data', labels={'Rat': 'Índice'}, 
                            title='Gráfico Minuto a Minuto - Audiência - Segunda a Sexta')

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("As colunas 'Hora', 'Rat' ou 'Data' não estão presentes no DataFrame.")

    with col2:
        st.title("Share")
        if 'Hora' in dfMinxMin and 'Shr' in dfMinxMin and 'Data' in dfMinxMin:

            # Use 'Data' para definir as cores ou marcadores para cada mês
            fig = px.scatter(dfMinxMin, x='Hora', y='Shr', color='Data', labels={'Shr': 'Índice'}, 
                            title='Gráfico Minuto a Minuto - Audiência - Segunda a Sexta')

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("As colunas 'Hora', 'Shr' ou 'Data' não estão presentes no DataFrame.")
    #Sabado
    #Domingo


if  __name__ == '__main__':
    sidebar()
    GraficoRanking()
    HistMensal()
    HistAnual()
    HistMinXMin()
    