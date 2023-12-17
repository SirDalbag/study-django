import uvicorn
import aiohttp
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
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


@app.post("/send")
async def send():
    TOKEN = "6397148691:AAG0QzG6dpDhGpoqETpkiwpQs2r4cWANL8w"
    users = "969075792"
    data = await CurrencyRate.get_currency_rate(filter=("USD", "EUR", "RUB"))
    msg = "\n".join(
        [
            f"Currency: {i['currency']}, Buy Price: {i['buy_price']}, Sell Price: {i['sell_price']}"
            for i in data
        ]
    )
    async with aiohttp.ClientSession() as session:
        for user in [str(x).strip() for x in users.split(",")]:
            async with session.get(
                f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                params={"chat_id": user, "text": msg},
            ) as response:
                await response.json()
    return RedirectResponse(url="/")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
