import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    todo = st.session_state["nova_tarefa"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("Meu app de Tarefas")
st.subheader("Este é meu app de tarefas a fazer.")
st.write("Este App é para aumentar sua produtividade.")


for todo in todos:
    st.checkbox(todo)


st.text_input(label="", placeholder="Digite uma tarefa...",
              on_change=add_todo, key='nova_tarefa')

print("Ola!!")