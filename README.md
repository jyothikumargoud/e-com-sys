# E-Commerce Competitor Monitoring System

## Overview

This project is a complete end-to-end automated data pipeline built for a B2B business use case.

The system collects product data from an e-commerce website, cleans and processes the information, stores it in a database, and exposes it through a dynamic dashboard and API.

The main goal of this project is to simulate how businesses monitor competitor products, pricing trends, customer reviews, and ratings automatically instead of manually checking websites every day.

This project demonstrates:

- Web scraping
- Data cleaning
- Database management
- Backend API development
- Dashboard creation
- Automation pipelines
- Deployment readiness

---

# Problem Statement

Many e-commerce businesses need competitor intelligence to make pricing and marketing decisions.

For example:

- A laptop seller may want to monitor competitor prices daily
- A retailer may want to identify highly rated products
- A business analyst may want to track customer review trends
- A sales team may want updated market data automatically

Manually collecting this information is:

- Time-consuming
- Error-prone
- Difficult to scale
- Impossible to keep updated continuously

This project solves that problem by building an automated competitor monitoring system.

---

# Business Use Case

This project is designed as a B2B solution.

The business value includes:

- Competitor price tracking
- Product comparison
- Market trend analysis
- Rating and review monitoring
- Automated data collection
- Real-time dashboard visibility

A business user can use this system to quickly understand:

- Which products are expensive
- Which products are popular
- Which categories perform better
- Market pricing patterns

---

# Data Source

The dataset is collected from the public test e-commerce website:

https://webscraper.io/test-sites/e-commerce/allinone

The scraper collects product data from categories such as:

- Laptops
- Tablets
- Phones

---

# Features

## Web Scraping

The scraper:

- Extracts product information automatically
- Handles missing values safely
- Prevents crashes during scraping
- Supports multiple product categories
- Exports structured raw JSON data

Extracted fields include:

- Product title
- Price
- Description
- Reviews
- Rating
- Category

---

## Data Cleaning

Raw scraped data is not immediately usable.

The cleaning pipeline:

- Removes duplicates
- Handles missing values
- Converts prices into numeric format
- Standardizes review counts
- Fixes inconsistent formatting
- Produces clean CSV files

This step ensures the data is reliable for analysis and storage.

---

## Database Storage

The cleaned data is stored inside SQLite.

SQLite was chosen because:

- Lightweight
- Easy to configure
- Good for small-to-medium pipelines
- Requires no external server setup

The database stores structured product records that can later be queried by APIs or dashboards.

---

## Automation

The entire pipeline is automated using APScheduler.

The automation system:

1. Runs the scraper
2. Cleans the data
3. Updates the database
4. Repeats automatically every 30 minutes

This ensures the system stays updated without manual intervention.

---

## Dashboard

A dynamic dashboard is built using FastAPI and Jinja templates.

The dashboard allows users to:

- View top products
- Compare prices
- See ratings and reviews
- Access live database information

The dashboard updates dynamically whenever new data enters the database.

---

## API Endpoint

The project also exposes API endpoints.

Example:

```bash
/api/products
```

This allows businesses or external systems to consume the data programmatically.


---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| BeautifulSoup | HTML parsing |
| Requests | HTTP requests |
| Pandas | Data cleaning and processing |
| SQLite | Database storage |
| FastAPI | Backend framework |
| Jinja2 | HTML templating |
| APScheduler | Automation |
| HTML/CSS | Frontend dashboard |

---

# Project Structure

```text
ecommerce-b2b-pipeline/
│
├── app.py
├── scraper.py
├── cleaner.py
├── database.py
├── scheduler.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── raw_products.json
│   └── cleaned_products.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── ecommerce.db
```

---

# Installation Guide

## Step 1 — Clone Repository

```bash
git clone <your-github-repo-url>
```

---

## Step 2 — Move into Project

```bash
cd ecommerce-b2b-pipeline
```

---

## Step 3 — Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Step 1 — Run Scraper

```bash
python scraper.py
```

This generates:

```text
data/raw_products.json
```

---

## Step 2 — Clean Data

```bash
python cleaner.py
```

This generates:

```text
data/cleaned_products.csv
```

---

## Step 3 — Store Data in Database

```bash
python database.py
```

This creates:

```text
ecommerce.db
```

---

## Step 4 — Run Dashboard

```bash
uvicorn app:app --reload
```

Open browser:

```text
http://127.0.0.1:8000
```

---

# Running Automation

To start the automated pipeline:

```bash
python scheduler.py
```

The scheduler automatically updates the pipeline every 30 minutes.

---

# API Endpoints

## Home Dashboard

```bash
/
```

Displays the product dashboard.

---

## Products API

```bash
/api/products
```

Returns all stored products in JSON format.

---

# Data Cleaning Decisions

Several preprocessing decisions were made to improve data quality.

## Price Cleaning

Prices originally contained `$` symbols.

Example:

```text
$699.99
```

Converted into numeric format:

```text
699.99
```

This allows mathematical operations and analysis.

---

## Missing Review Values

Some products had missing review counts.

Missing values were replaced with:

```text
0
```

This prevents crashes during processing.

---

## Duplicate Removal

Duplicate product records were removed to improve database quality.

---

## Missing Descriptions

Products without descriptions were replaced with:

```text
No Description
```

---

# Error Handling

The scraper includes error handling for:

- Failed requests
- Missing HTML elements
- Timeout errors
- Parsing failures

This ensures the scraper continues running even if some products fail.

---

# Why FastAPI Was Chosen

FastAPI was selected because:

- Fast performance
- Simple API development
- Easy deployment
- Automatic documentation support
- Good scalability

It is commonly used in production-grade backend systems.

---

# Why SQLite Was Chosen

SQLite is suitable for this assignment because:

- No separate server needed
- Easy local setup
- Lightweight
- Fast for small pipelines

For large-scale production systems, PostgreSQL would be a better choice.

---

# Future Improvements

Several enhancements can be added in future versions:

- Product search functionality
- Filtering by category
- Interactive charts
- Authentication system
- PostgreSQL integration
- Docker support
- Cloud deployment
- Real-time analytics
- AI-based price prediction
- Competitor comparison engine

---

# Challenges Faced

Some challenges encountered during development:

- Handling missing review values
- Converting price strings into numeric values
- Managing FastAPI template compatibility
- Cleaning inconsistent scraped data
- Automating the pipeline safely

These issues were resolved through validation and preprocessing logic.

---

# Learning Outcomes

This project helped improve understanding of:

- Web scraping pipelines
- Data preprocessing
- Backend API development
- Database integration
- Automation systems
- Dynamic dashboards
- Production-oriented project structure

---

# Conclusion

This project demonstrates how automated data pipelines can help businesses collect and monitor competitor information efficiently.

The final system provides:

- Automated scraping
- Reliable data cleaning
- Structured storage
- Dynamic dashboards
- API access
- Continuous updates

The architecture is modular, scalable, and suitable as a foundation for more advanced business intelligence systems.
