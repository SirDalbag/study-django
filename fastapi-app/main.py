import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utilities import Weather

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "weather": Weather.get_weather()}
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
