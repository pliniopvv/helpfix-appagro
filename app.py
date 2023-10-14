import streamlit as st
from login import LoginApp
from data_invest import DataInvestApp

class App:
    def __init__(self):
        self.login_app = LoginApp()  # Crie uma instância de LoginApp
        st.session_state.logged_in = False # Use o atributo logged_in de LoginApp

    def run(self):
        if not st.session_state.logged_in:
            self.login_app.run()


if __name__ == "__main__":
    app = App()
    app.run()