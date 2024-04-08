from fastapi import FastAPI
from pydantic import BaseModel
from database.queries import execute
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    first_name: str
    last_name: str
    age: int


@app.get("/api/users/")
async def get_users():
    return await execute(
        query="SELECT user_id, first_name, last_name, age FROM users", method="GET"
    )


@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    return await execute(
        query="SELECT first_name, last_name, age FROM users WHERE user_id = $1",
        method="GET",
        args=(user_id,),
    )


@app.post("/api/user/")
async def post_user(user: User):
    return await execute(
        query="CALL new_user($1, $2, $3)",
        method="POST",
        args=(user.first_name, user.last_name, user.age),
    )
