# app.py

#import the library
import streamlit as st

# add title to your app
st.title("Hello world!")
st.write('That\'s my very first streamlit web app!')

st.slider("How good is this web app?", 0, 10)
