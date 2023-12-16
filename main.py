from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # すべてのオリジンを許可
    allow_credentials=True,
    allow_methods=["*"],  # すべてのHTTPメソッドを許可
    allow_headers=["*"],  # すべてのHTTPヘッダーを許可
)

class TodoItem(BaseModel):
    id: int
    text: str
    completed: bool

todos: List[TodoItem] = []

@app.get("/todos", response_model=List[TodoItem])
async def read_todos():
    return todos

@app.post("/todos", response_model=TodoItem)
async def create_todo(todo_item: TodoItem):
    todos.append(todo_item)
    return todo_item

@app.put("/todos/{todo_id}", response_model=TodoItem)
async def update_todo(todo_id: int, todo_item: TodoItem):
    for index, item in enumerate(todos):
        if item.id == todo_id:
            todos[index] = todo_item
            return todo_item
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    global todos
    todos = [item for item in todos if item.id != todo_id]
    return {"message": "Todo deleted successfully"}
