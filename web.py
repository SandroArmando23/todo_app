import streamlit as st

from modules import functions

todos = functions.get_todos()


st.title("My To-Do App")
st.subheader("This is my To-Do App")
st.write("This App will increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo:", placeholder="Add new todo...")

