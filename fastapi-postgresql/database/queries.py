from dotenv import load_dotenv
import asyncpg
import os

load_dotenv()

DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")

DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"


async def execute(query: str, method: str, args: tuple = None):
    connection = await asyncpg.connect(DATABASE_URL)
    try:
        if method in ["GET"]:
            data = (
                await connection.fetch(query, *args)
                if args
                else await connection.fetch(query)
            )
            return {"data": data}
        elif method in ["POST", "PUT", "PATCH", "DELETE"]:
            await connection.execute(query, *args)
            return {"message": "success"}
    except Exception as error:
        return {"message": f"{error}"}
    finally:
        connection.close()
