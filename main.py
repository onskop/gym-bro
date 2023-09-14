import streamlit as st
import os

with os.open("novejfile.txt", "r") as f:
    data = f.read()


st.write(data)
