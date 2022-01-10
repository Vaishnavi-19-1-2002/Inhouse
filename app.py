import streamlit as st
import requests
import pandas as pd

name = st.text_input("Username")
password = st.text_input("Password", type="password")
button = st.button("Submit")

if button:
    data = {
        'uname':name,
        'password':password
    }
    res = requests.post('http://127.0.0.1:5000/login', data)
    st.success("Pushed data successfully.")
    showData = st.button("Show Data")
    
    
    df = pd.read_csv("data_file.csv")
    st.title("Data")
    st.table(df)

