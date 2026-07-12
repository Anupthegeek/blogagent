import streamlit as st

st.set_page_config(page_title="My Blog", layout="wide")

with open("blog_post.md", "r", encoding="utf-8") as f:
    content = f.read()

st.markdown(content)
