import streamlit as st
import functions


todos=functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("To-Do App")
st.subheader("Manage your everyday/week/month activities")
st.write("Increase your productivity with smart event-management")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]

st.text_input(label = "To-Do Inputer",
              on_change=add_todo,
              placeholder="Add a new todo...",
              key="new_todo")
