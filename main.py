from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from todo import todo_router

app = FastAPI()

origins = [
    "http://127.0.0.1:5501", "http://54.196.26.53:8001"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def welcome() -> dict:
    return {
        "msg": "Welcome to FastAPI!"
    }

app.include_router(todo_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)