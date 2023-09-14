import streamlit as st
import os

# read file content
with open('novejfile.txt', 'r') as f:
    data = f.read()


st.write(data)
