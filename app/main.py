from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import requests
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# تنظیم قالب‌های HTML و استاتیک‌ها
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


# مدل برای درخواست تبدیل ارز
class ConversionRequest(BaseModel):
    from_currency: str
    to_currency: str
    amount: float


# آدرس API خارجی (مثلاً Fixer.io یا Open Exchange Rates)
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"


# تابع برای دریافت نرخ‌های تبدیل ارز
def get_exchange_rates():
    response = requests.get(API_URL)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="خطا در دریافت نرخ‌های تبدیل ارز")
    return response.json()


@app.get("/")
async def read_root(request: Request):
    """صفحه اصلی"""
    data = get_exchange_rates()
    return templates.TemplateResponse("index.html", {"request": request, "rates": data["rates"]})


@app.post("/convert")
async def convert_currency(request: ConversionRequest):
    """یک ارز را به ارز دیگر تبدیل می‌کند"""
    data = get_exchange_rates()
    from_currency = request.from_currency.upper()
    to_currency = request.to_currency.upper()

    if from_currency not in data["rates"] or to_currency not in data["rates"]:
        raise HTTPException(status_code=400, detail="ارز نامعتبر")

    conversion_rate = data["rates"][to_currency] / data["rates"][from_currency]
    converted_amount = request.amount * conversion_rate
    return {"converted_amount": converted_amount, "from_currency": from_currency, "to_currency": to_currency}
