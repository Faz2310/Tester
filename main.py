import streamlit as st

st.title('Hello World')
st.write('This Is A simple Streamlit App')

st.chat_input("Enter Your Input")
if input == 'what are you doing':
    st.write('Im Doing Work')

if st.button('Hello'):
    st.write("Hello from streamlit")

name = st.text_input('Enter Your name')

if name!='':
    st.write(f'Hello{name}')
