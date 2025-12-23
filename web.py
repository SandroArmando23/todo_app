import streamlit as st

from modules import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n" # session_state crea un simil-dizionario
    todos.append(todo)
    functions.write_todos(todos)

st.title("My To-Do App")
st.subheader("This is my To-Do App")
st.write("This App will increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo:", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

