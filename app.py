from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from scraper import scrape_data
from cleaner import clean_data
from database import create_database, insert_data

import sqlite3
import os

# -----------------------------------
# CREATE REQUIRED FOLDERS
# -----------------------------------

os.makedirs("data", exist_ok=True)
os.makedirs("templates", exist_ok=True)
os.makedirs("static", exist_ok=True)

# -----------------------------------
# FASTAPI APP
# -----------------------------------

app = FastAPI()

# -----------------------------------
# STATIC FILES
# -----------------------------------

app.mount("/static", StaticFiles(directory="static"), name="static")

# -----------------------------------
# TEMPLATES
# -----------------------------------

templates = Jinja2Templates(directory="templates")

# -----------------------------------
# DATABASE
# -----------------------------------

DB_NAME = "ecommerce.db"

# -----------------------------------
# STARTUP EVENT
# -----------------------------------

@app.on_event("startup")
async def startup_event():

    print("Starting automated pipeline...")

    try:
        scrape_data()

        clean_data()

        create_database()

        insert_data()

        print("Pipeline completed successfully!")

    except Exception as e:
        print(f"Startup pipeline failed: {e}")

# -----------------------------------
# HOME DASHBOARD
# -----------------------------------

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):

    try:
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

        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "products": products
            }
        )

    except Exception as e:

        return HTMLResponse(
            content=f"""
            <h1>Application Error</h1>
            <p>{str(e)}</p>
            """,
            status_code=500
        )

# -----------------------------------
# API ENDPOINT
# -----------------------------------

@app.get("/api/products")
async def get_products():

    try:

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

    except Exception as e:

        return {
            "error": str(e)
        }