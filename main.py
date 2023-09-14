import streamlit as st
import os
import numpy as np
import pandas as pd

# read file content
with open('textdata.txt', 'r', encoding='utf-8') as f:
    data = f.read()

# write file content

st.markdown("""
<style>
.big-font {
    font-size:30px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">{0}</p>'.format(data), unsafe_allow_html=True)


path = 'res'
files = os.listdir(path)
index = st.slider('Vyber si svého bro!', 0, len(files)-1, 0)
st.image(os.path.join(path, files[index]), use_column_width=True)


df1 = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

if st.sidebar.checkbox('Show dataframe'):
    df2 = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
    st.dataframe(df2.style.highlight_max(axis=0))
    if st.sidebar.checkbox('Show chart'):
        st.line_chart(df2)


# text field for input
user_input = st.text_input("Napiš prompt", "Ale tenhle prompt teď stejně nic nedělá")
st.write('Napsal jsi: ', user_input)
