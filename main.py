import streamlit as st
import os

# read file content
with open(os.path.join(os.path.dirname(__file__), 'novejfile.txt'), 'r') as f:
    data = f.read()


st.write(data)
