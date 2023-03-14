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


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="", placeholder="Digite uma tarefa...",
              on_change=add_todo, key='nova_tarefa')

