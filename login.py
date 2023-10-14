import sqlite3
import streamlit as st
from data_invest import DataInvestApp

class LoginApp:
    def __init__(self):
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                email TEXT,
                senha TEXT
            )
        """)
        conn.commit()
        conn.close()

    def insert_user(self, nome, email, senha):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
        conn.commit()
        conn.close()

    def check_login(self, email, senha):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ? AND senha = ?", (email, senha))
        user = cursor.fetchone()
        conn.close()
        return user

    def clear_page(self):
        st.write("")  # Isso limpa o conteúdo atual

    def run(self):
        # Título do painel
        st.title("Painel de Login e Cadastro")

        # Opção de seleção para escolher entre Login e Cadastro
        choice = st.sidebar.selectbox("Escolha uma opção:", ["Login", "Cadastro"])

        # Variável para controlar a exibição da mensagem de erro
        erro_login = False

        # Se a opção escolhida for "Cadastro"
        if choice == "Cadastro":
            st.subheader("Crie uma nova conta")

            # Formulário de cadastro
            nome = st.text_input("Nome")
            email = st.text_input("Email")
            senha = st.text_input("Senha", type="password")
            confirm_senha = st.text_input("Confirme a senha", type="password")

            # Validar se as senhas coincidem apenas se houver algo escrito nas caixas de senha
            if senha and confirm_senha:
                if senha == confirm_senha:
                    st.success("Senhas coincidem!")

            # Botão de cadastro
            if st.button("Cadastrar"):
                # Salvar os dados do novo usuário no banco de dados
                self.insert_user(nome, email, senha)
                st.success("Cadastro realizado com sucesso!")

        # Se a opção escolhida for "Login"
        elif choice == "Login":
            st.subheader("Faça login na sua conta")

            # Formulário de login
            email = st.text_input("Email")
            senha = st.text_input("Senha", type="password")

            # Botão de login
            if st.button("Entrar"):
                # Limpar a tela antes de iniciar o DataInvestApp
                self.clear_page()
                # Verificar o login
                user = self.check_login(email, senha)
                
                if user:
                    # Exibir mensagem de sucesso
                    st.success(f"Bem-vindo, {user[1]}!")  # Exibe o nome do usuário após o login
                    data_invest_app = DataInvestApp()
                    data_invest_app.run()
                else:
                    # Exibir mensagem de erro
                    st.error("Email ou senha incorretos. Tente novamente.")


