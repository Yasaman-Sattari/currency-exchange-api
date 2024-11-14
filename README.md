# Currency Exchange API

## توضیحات
این پروژه یک API برای پیش‌بینی قیمت ارز است که از داده‌های به‌روز استفاده می‌کند. شما می‌توانید نرخ‌های تبدیل ارز بین ارزهای مختلف را دریافت کرده و یک ارز را به ارز دیگری تبدیل کنید.

## ویژگی‌ها
- دریافت نرخ‌های تبدیل ارز به‌روز.
- تبدیل ارز از یک ارز به ارز دیگر.
- طراحی زیبا با استفاده از HTML و CSS.

## نحوه اجرا
1. ابتدا محیط مجازی را فعال کرده و وابستگی‌ها را نصب کنید:
   ```bash
   pip install -r requirements.txt


سپس سرور FastAPI را اجرا کنید:
uvicorn app.main:app --reload
به http://127.0.0.1:8000 بروید و از فرم برای تبدیل ارز استفاده کنید.

API Endpoints
GET /: صفحه اصلی که نرخ‌های تبدیل ارز را نمایش می‌دهد.
POST /convert: برای تبدیل یک ارز به ارز دیگر.



Currency Exchange Prediction API Project

This project is a simple yet powerful Currency Exchange API built using FastAPI, designed to provide real-time currency conversion rates between different currencies. The API allows users to input a source currency and a target currency, and it returns the live exchange rate between the two currencies. It’s a practical tool for anyone needing quick access to up-to-date currency exchange information.

The system is built with a strong emphasis on clean code and scalability. Following Object-Oriented Programming (OOP) principles, the code is modular, maintainable, and well-structured, ensuring that it can be easily extended with additional features in the future. The API fetches live exchange rate data from an external data provider, ensuring that users always have access to the latest rates.

The project also includes a front-end interface that allows users to interact with the API through a simple, user-friendly web page. The interface is designed using HTML and CSS to create an aesthetically pleasing and responsive experience. The web page allows users to input their desired currencies, view the exchange rate, and perform conversions directly from the browser.

Key Features:

Real-time currency exchange rates.
Support for a wide range of currencies.
Simple, intuitive front-end built with HTML and CSS.
Modular back-end with FastAPI, ensuring scalability and flexibility.
Data fetched from a reliable external API provider, ensuring accuracy.
This project serves as a great example of how to integrate backend APIs with front-end interfaces. It demonstrates how real-time data can be fetched, displayed, and used to power interactive applications. Whether you’re a developer looking to learn more about FastAPI, or a user needing to convert currencies on the go, this project offers a clean, functional, and professional solution.

The Currency Exchange API is perfect for anyone looking to implement real-time data fetching and API integration in their projects.

