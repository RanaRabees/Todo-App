# # 3. Implement Streamlit Client
# # streamlit_client.py

from database import Session, Todo
import streamlit as st
import random

BASE_URL = "http://127.0.0.1:8000"
db: Session = Session()

def generate_unique_number(length=4):
  """ Generates a random unique number of the specified length. """

  while True:
    number = "".join(str(random.randint(0, 4)) for _ in range(length))
    if number[0] != "0":
      return number

def get_todos():
    """ Retrieves a list of all todos. """
    try:
        todos = db.query(Todo).all()
        st.write("**List of Todos:**")
        for todo in todos:
            st.write(f"- **{todo.id}.** {todo.title}: {todo.description}")
    except Exception as e:
        st.error(f"Error retrieving todos: {e}")
    finally:
        db.close()
        
def create_todo():
    """ Creates a new todo. """
    title = st.text_input("Enter Todo Title")
    description = st.text_area("Enter Todo Description")
    if st.button("Add Todo"):
        try:
            unique_number = generate_unique_number()
            todo = Todo(id = unique_number, title=title, description=description)
            db.add(todo)
            db.commit()
            st.success(f"Todo added successfully! And your id is: {unique_number} Kindly! Save This!")
        except Exception as e:
            st.error(f"Error adding todo: {e}")
            
# def update_todo():
#     """ Updates an existing todo. """
#     with Session() as db:
#         todo_id = st.number_input('Enter Todo ID to update...', value=1, step=1)
#         if st.button("Update Todo"):
#             with st.form("update_form"):
#                 title = st.text_input("Enter New Title (optional)")
#                 description = st.text_area("Enter New Description (optional)")
#                 submitted = st.form_submit_button("Submit Update")

#                 if submitted:
#                     try:
#                         todo_to_update = db.query(Todo).filter(Todo.id == todo_id).first()
#                         st.write("Forwarding")
#                         if todo_to_update:
#                             todo_to_update.title = title or todo_to_update.title
#                             todo_to_update.description = description or todo_to_update.description
#                             db.add(todo_to_update)
#                             db.commit()
#                             st.success("Todo updated successfully")
#                         else:
#                             raise ValueError("Todo not found")
#                     except Exception as e:
#                         st.error(f"Error updating todo: {e}")     
  
def delete_todo():
    """ Deletes a todo. """
    # todo_id = st.number_input('Enter Todo ID to delete...', value=1, step=1)
    todo_id = st.text_input('Enter Todo ID to delete...')
    if st.button("Delete Todo"):
        try:
            todo_to_delete = db.query(Todo).filter(Todo.id == todo_id).first()
            if todo_to_delete:
                db.delete(todo_to_delete)
                db.commit()
                st.success("Todo deleted successfully")
            else:
                raise ValueError("Todo not found")
        except Exception as e:
            st.error(f"Error deleting todo: {e}")

if __name__ == "__main__":
    st.title("Todo App")
    st.write("This project is simple Todo App implemented using FastAPI, SQLAlchemy and Streamlit. It provides basic functionality for managing tasks, allowing you to perform operations such as retrieving tasks (GET), adding new tasks (POST), and deleting tasks (DELETE).")
    st.markdown("#### Get()")
    get_todos()
    st.markdown("#### Post()")
    create_todo()
    # st.markdown("#### Put()")
    # update_todo()
    st.markdown("#### Delete()")
    delete_todo()
