import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utilities import Weather, CurrencyRate, CurrencyRateAPI

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "weather": await Weather.get_weather(),
            "currency_rate": await CurrencyRate.get_currency_rate(
                filter=("USD", "EUR", "RUB")
            ),
            "currency_rate_api": await CurrencyRateAPI.get_currency_rate(),
        },
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
