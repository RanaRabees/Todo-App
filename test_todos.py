import pytest
from fastapi.testclient import TestClient
from main import app
from database import Session, Todo

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="function")
def clear_database():
    db = Session()
    try:
        db.query(Todo).delete()
        db.commit()
    finally:
        db.close()

def test_get_todos(clear_database):
    """Tests retrieving todos, both when empty and with existing todos."""

    # Test when database is empty
    db = Session()
    todos = db.query(Todo).all()
    assert todos == []
    db.close()

    # Test when todos exist
    db = Session()
    todo1 = Todo(title="Todo 1", description="First todo")
    todo2 = Todo(title="Todo 2", description="Second todo")
    db.add_all([todo1, todo2])
    db.commit()

    todos = db.query(Todo).all()
    assert todos == [todo1, todo2]
    assert len(todos) == 2
    db.close()

def test_create_todo(clear_database):
    db = Session()
    new_todo = Todo(title="Test Todo", description="This is a test todo")
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    todos = db.query(Todo).all()
    assert todos == [new_todo]
    assert new_todo.id is not None
    db.close()

# def test_update_todo(clear_database):
#     db = Session()
#     todo = Todo(title="Original Title", description="Original Description")
#     db.add(todo)
#     db.commit()
#     todo_id = todo.id

#     updated_data = {"title": "Updated Title", "description": "Updated Description"}
#     db.query(Todo).filter(Todo.id == todo_id).update(updated_data)
#     db.commit()

#     updated_todo = db.query(Todo).filter(Todo.id == todo_id).first()
#     assert updated_todo.title == updated_data["title"]
#     assert updated_todo.description == updated_data["description"]
#     db.close()

def test_delete_todo(clear_database):
    db = Session()
    todo = Todo(title="Todo to Delete", description="This will be deleted")
    db.add(todo)
    db.commit()
    todo_id = todo.id

    db.delete(todo)
    db.commit()

    deleted_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    assert deleted_todo is None
    db.close()
