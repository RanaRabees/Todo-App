

# # 2. Create FastAPI CRUD Endpoints
# # main.py

from typing import List
# from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException, Depends
from database import Session, Todo
from pydantic import BaseModel

app = FastAPI()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@app.get("/hi")
def greet():
    return "Hello! World!"

@app.get("/hi/{name}")
def greet_with_name(name: str):
    return "Hello! World, " + name

class Todo(BaseModel):
    id: int
    title: str
    description: str

@app.get("/todos", response_model=List[Todo])
def get_todos(db: Session = Depends(get_db)):
    try:
        todos = db.query(Todo).all()
        return todos
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving todos: {e}")

@app.post("/todos")
def create_todo(todo: Todo, db: Session = Depends(get_db)):
    db_todo = Todo(**todo.dict())
    # db_todo.id = None
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# @app.put("/todos/{todo_id}")
# def update_todo(todo_id: int, updated_todo: Todo, db: Session = Depends(get_db)):
#     try:
#         db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
#         if db_todo is None:
#             raise HTTPException(status_code=404, detail="Todo not found")

#         for key, value in updated_todo.dict(exclude_unset=True).items():
#             setattr(db_todo, key, value)

#         db.add(db_todo)
#         db.commit()
#         return db_todo
#     except Exception as e:
#         db.rollback()
#         raise HTTPException(status_code=500, detail=f"Error updating todo: {str(e)}")  # Re-raise with a more informative message
#     finally:
#         db.close()

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted"}



