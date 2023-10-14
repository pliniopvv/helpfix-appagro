import datetime
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
import os

st.set_page_config(layout="wide")  # Tornar a página estática

class DataInvestApp:
    def __init__(self):
        # Título do aplicativo
        st.title("Painel Interativo de Análise de Datas")

        # Sidebar para seleção de arquivo CSV
        st.sidebar.header("Selecione um Arquivo CSV")
        csv_files = [f for f in os.listdir("./csv") if f.endswith(".csv")]  # Lista todos os arquivos CSV no diretório

        if not csv_files:
            st.error("Nenhum arquivo CSV encontrado no diretório './csv'.")
            st.stop()

        self.selected_file = st.sidebar.selectbox("Escolha um arquivo:", csv_files)  # Altere o diretório conforme necessário

        try:
            separator = st.sidebar.text_input("Digite o separador (ex: , ou ;)", ";")  # Pergunte ao usuário pelo separador
            self.df = pd.read_csv(os.path.join("csv", self.selected_file), sep=separator)
            self.df['DATAf'] = pd.to_datetime(self.df['DATA'], format="%d/%m/%Y")
        except Exception as e:
            st.error(f"Erro ao carregar o arquivo CSV: {e}")
            st.stop()

    def run(self):
        # Sidebar para filtros de data
        st.sidebar.header("Filtros")
        
        min_date = self.df['DATAf'].min()
        max_date = self.df['DATAf'].max()

        min_datef = datetime.date(min_date.year, min_date.month, min_date.day)
        max_datef = datetime.date(max_date.year, max_date.month, max_date.day)

        start_date = st.sidebar.date_input("Data de Início", value = min_datef, min_value=min_datef, max_value=max_datef)
        end_date = st.sidebar.date_input("Data de Término", value = min_datef, min_value=min_datef, max_value=max_datef)

        # Botão "Validar"
        if st.sidebar.button("Validar"):
            # Filtrar os dados com base nas datas selecionadas
            filtered_df = self.df[(self.df['Data'] >= start_date) & (self.df['Data'] <= end_date)]

            # Exibir os dados filtrados
            st.write("### Dados Filtrados:")
            st.write(filtered_df)

            # Gráfico de Linha Interativo
            st.write("### Gráfico de Linha Interativo")
            fig_line = go.Figure()
            fig_line.add_trace(go.Scatter(x=filtered_df['Data'], y=filtered_df['Valor'], mode='lines+markers', name='Valor'))
            fig_line.update_layout(title="Variação do Valor ao Longo do Tempo", xaxis_title="Data", yaxis_title="Valor")
            st.plotly_chart(fig_line)

            # Gráfico de Barras Interativo
            st.write("### Gráfico de Barras Interativo")
            fig_bar = px.bar(filtered_df, x='Data', y='Quantidade', title="Quantidade ao Longo do Tempo")
            st.plotly_chart(fig_bar)

            # Estatísticas Resumidas
            st.write("### Estatísticas Resumidas")
            st.write(filtered_df.describe())

        # Rodapé
        st.sidebar.write("Desenvolvido por [Seu Nome]")

if __name__ == "__main__":
    app = DataInvestApp()
    app.run()