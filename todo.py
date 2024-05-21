from fastapi import APIRouter, Path
from model import Todo

todo_router = APIRouter()

todo_list = []

@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {
        "todos" : todo_list
    }

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo.id = len(todo_list)+1
    todo_list.append(todo)
    return {
        "msg" : "todo add success"
    }
    
@todo_router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int = Path(..., title="the ID of the todo to delete")) -> dict:
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            del todo_list[index]
            return {"msg": f"Todo with ID {todo_id} deleted successfully"}
    return {"msg": "Todo with supplied ID doesn't exist"}

    
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="id")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo" : todo
            }
    return {
        "msg" : "todo not found"
    }