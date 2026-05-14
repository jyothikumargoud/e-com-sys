from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import sqlite3

app = FastAPI()

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

DB_NAME = "ecommerce.db"


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT title, price, reviews, rating
        FROM products
        ORDER BY price DESC
        LIMIT 20
    """)

    products = cursor.fetchall()

    conn.close()

    # IMPORTANT FIX HERE
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "products": products
        }
    )


@app.get("/api/products")
async def get_products():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM products
    """)

    rows = cursor.fetchall()

    conn.close()

    return {
        "products": rows
    }

