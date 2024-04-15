from sanic import Sanic
from sanic_ext import Extend
from sanic.response import json
from pydantic import BaseModel
from database.queries import execute

app = Sanic("UsersAPI")

app.config.CORS_ORIGINS = "http://localhost:3000"
Extend(app)


class User(BaseModel):
    first_name: str
    last_name: str
    age: int


@app.route("/api/users", methods=["GET"], name="get_users")
async def get_users(request):
    users = await execute(
        query="SELECT user_id, first_name, last_name, age FROM users", method="GET"
    )
    if users.get("data"):
        data = []
        for user in users["data"]:
            data.append(
                {
                    "user_id": user[0],
                    "first_name": user[1],
                    "last_name": user[2],
                    "age": user[3],
                }
            )
        return json({"data": data})
    return json({"message": users["message"]})


@app.route("/api/users/<user_id:int>", methods=["GET"], name="get_user")
async def get_user(request, user_id):
    user = await execute(
        query="SELECT first_name, last_name, age FROM users WHERE user_id = $1",
        method="GET",
        args=(user_id,),
    )
    if user.get("data"):
        user = user["data"][0]
        data = {
            "first_name": user[0],
            "last_name": user[1],
            "age": user[2],
        }
        return json({"data": data})
    return json({"message": user["message"]})


@app.route("/api/users", methods=["POST"], name="post_users")
async def post_user(request):
    user_data = request.json
    user = User(**user_data)
    status = await execute(
        query="CALL new_user($1, $2, $3)",
        method="POST",
        args=(user.first_name, user.last_name, user.age),
    )
    return json({"message": status["message"]})


@app.route("/api/users/<user_id:int>", methods=["PUT"], name="edit_users")
async def edit_user(request, user_id):
    user_data = request.json
    user = User(**user_data)
    status = await execute(
        query="CALL edit_user($1, $2, $3, $4)",
        method="PUT",
        args=(user_id, user.first_name, user.last_name, user.age),
    )
    return json({"message": status["message"]})


@app.route("/api/users/<user_id:int>", methods=["DELETE"], name="delete_users")
async def delete_user(request, user_id):
    status = await execute(
        query="CALL delete_user($1)",
        method="DELETE",
        args=(user_id,),
    )
    return json({"message": status["message"]})
