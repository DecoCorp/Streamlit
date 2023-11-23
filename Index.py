# Importando as libs
import streamlit as st
import os
import pandas as pd
import plotly.express as px
from PIL import Image
import matplotlib.pyplot as plt

# Configurar o layout da página
st.set_page_config(layout="wide")

def highlight_missing_data(val):
    return 'background-color: #ffcccc' if pd.isnull(val) else ''

# Criando o sidebar
def sidebar():
    sidebar = st.sidebar
    # logo + data
    logo = "img/tv_bahia_BRANCA.png"
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
    # Configuração do estilo com fundo preto para o Matplotlib
    plt.style.use('dark_background')
    
    st.markdown("<h1 style='text-align: center;'>HISTÓRICO MENSAL</h1>", unsafe_allow_html=True)
    
    dadosHistMensal = pd.read_csv('dados/historico_mensal_preparado_0612_2023_5.csv')
    dfHistMensal = pd.DataFrame(dadosHistMensal)

    col1, col2 = st.columns(2)
    # 06h às 12h
    with col1:
        st.title("Audiência")
        if 'Emissora' in dfHistMensal and 'Rat' in dfHistMensal and 'Data' in dfHistMensal:
            st.write("Histórico Mensal - Audiência - 06h às 12h")

            # Criar um gráfico de linha com fundo preto
            plt.figure(figsize=(10, 6))
            for emissora in dfHistMensal['Emissora'].unique():
                dados_emissora = dfHistMensal[dfHistMensal['Emissora'] == emissora]
                plt.plot(dados_emissora['Data'].to_numpy(), dados_emissora['Rat'].to_numpy(), label=emissora, marker='o')

            plt.title("Histórico Mensal - Audiência - 06h às 12h")
            plt.xlabel("Mês")
            plt.ylabel("Rat")
            plt.legend()
            plt.xticks(rotation=45, ha='right')  # Rotacionar rótulos de mês para melhor legibilidade
            st.pyplot()
        else:
            st.warning("As colunas 'Emissora', 'Rat' ou 'Data' não estão presentes no DataFrame.")
    with col2:
        st.title('Share')
        if 'Emissora' in dfHistMensal and 'Shr' in dfHistMensal and 'Data' in dfHistMensal:
            st.write("Histórico Mensal - Share - 06h às 12h")

            # Criar um gráfico de linha com fundo preto
            plt.figure(figsize=(10, 6))
            for emissora in dfHistMensal['Emissora'].unique():
                dados_emissora = dfHistMensal[dfHistMensal['Emissora'] == emissora]
                plt.plot(dados_emissora['Data'].to_numpy(), dados_emissora['Shr'].to_numpy(), label=emissora, marker='o')

            plt.title("Histórico Mensal - Share - 06h às 12h")
            plt.xlabel("Mês")
            plt.ylabel("Share")
            plt.legend()
            plt.xticks(rotation=45, ha='right')  # Rotacionar rótulos de mês para melhor legibilidade
            st.pyplot()
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
    
    fig, ax = plt.subplots(figsize=(10, 6))

    nomes_emissoras_unicos = set()
    
    col1, col2 = st.columns(2)  # Criar duas colunas
    with col1:
        st.title("Audiência")
        if 'Emissoras' in dfHistAnual and 'Rat' in dfHistAnual and 'Datas' in dfHistAnual:
            st.markdown("<h5 style='text-align: center;'>Gráfico Histórico Anual - Audiência</h5>", unsafe_allow_html=True)

            # Criar uma figura e eixos do Matplotlib
            fig, ax = plt.subplots(figsize=(8, 6))

            # Plotar as linhas
            for coluna in dfHistAnual.columns:
                    if coluna != 'Índice' and coluna != 'Emissora':
                        # Verificar se o nome da emissora ainda não foi visto
                        if coluna not in nomes_emissoras_unicos:
                            ax.plot(dfHistAnual['Data'].to_numpy(), dfHistAnual[coluna], label=coluna, marker='o')
                            nomes_emissoras_unicos.add(coluna)

            # Adicionar rótulos e legenda
            ax.set_title("Gráfico de Linha para Múltiplas Colunas")
            ax.set_xlabel("Data")
            ax.set_ylabel("Valores")
            ax.legend()

            # Mostrar o gráfico no Streamlit
            st.pyplot(fig)
        else:
            st.warning("As colunas 'Emissoras', 'Rat' ou 'Datas' não estão presentes no DataFrame.")

    with col2:
        st.title("Share")
        if 'Emissoras' in dfHistAnual and 'Shr' in dfHistAnual and 'Datas' in dfHistAnual:
            st.markdown("<h5 style='text-align: center;'>Gráfico Histórico Anual - Share</h5>", unsafe_allow_html=True)

            # Criar uma figura e eixos do Matplotlib
            fig, ax = plt.subplots(figsize=(8, 6))

            # Plotar as linhas
            for emissora in dfHistAnual['Emissoras'].unique():
                dados_emissora = dfHistAnual[dfHistAnual['Emissoras'] == emissora]
                ax.plot(dados_emissora['Datas'].to_numpy(), dados_emissora['Shr'], label=emissora, marker='o')

            # Adicionar rótulos e legenda
            ax.set_xlabel('Datas')
            ax.set_ylabel('Shr')
            ax.set_title('Gráfico Histórico Anual - Share')
            ax.legend()

            # Mostrar o gráfico no Streamlit
            st.pyplot(fig)
        else:
            st.warning("As colunas 'Emissoras', 'Shr' ou 'Datas' não estão presentes no DataFrame.")


    # Historico min a min dia completo (audiência x share)
def HistMinXMin():
    # Segunda
    st.markdown("<h1 style='text-align: center;'>MINUTO A MINUTO DIA COMPLETO</h1>", unsafe_allow_html=True)

    DadosMinXMin = pd.read_csv('dados/minuto_minuto_preparado_ss_5.csv')
    dfMinxMin = pd.DataFrame(DadosMinXMin)

    col1, col2 = st.columns(2)  # Criar duas colunas
    with col1:
        st.title("Audiência")
        if 'Hora' in dfMinxMin and 'Rat' in dfMinxMin and 'Data' in dfMinxMin:
            plt.figure(figsize=(10, 6))

            # Use 'Data' para definir as cores ou marcadores para cada mês
            for data, group in dfMinxMin.groupby('Data'):
                plt.scatter(group['Hora'], group['Rat'], label=data)

            plt.title('Gráfico Minuto a Minuto - Audiência - Segunda a Sexta')
            plt.xlabel('Hora')
            plt.ylabel('Índice')
            plt.legend()
            st.pyplot()

        else:
            st.warning("As colunas 'Hora', 'Rat' ou 'Data' não estão presentes no DataFrame.")

    with col2:
        st.title("Share")
        if 'Hora' in dfMinxMin and 'Shr' in dfMinxMin and 'Data' in dfMinxMin:
            plt.figure(figsize=(10, 6))

            # Use 'Data' para definir as cores ou marcadores para cada mês
            for data, group in dfMinxMin.groupby('Data'):
                plt.scatter(group['Hora'], group['Shr'], label=data)

            plt.title('Gráfico Minuto a Minuto - Audiência - Segunda a Sexta')
            plt.xlabel('Hora')
            plt.ylabel('Índice')
            plt.legend()
            st.pyplot()

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

