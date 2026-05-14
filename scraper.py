import requests
from bs4 import BeautifulSoup
import json
import logging
from time import sleep

logging.basicConfig(level=logging.INFO)

BASE_URL = "https://webscraper.io/test-sites/e-commerce/allinone"

CATEGORIES = [
    "/computers/laptops",
    "/computers/tablets",
    "/phones/touch"
]

def scrape_page(url):
    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            logging.error(f"Failed: {url}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")

        products = soup.find_all("div", class_="thumbnail")

        page_data = []

        for product in products:
            try:
                title = product.find("a", class_="title")
                price = product.find("h4", class_="price")
                description = product.find("p", class_="description")
                reviews = product.find("p", class_="pull-right")
                rating = product.find_all("span", class_="glyphicon-star")



                item = {
    "title": title.text.strip() if title else None,
    "price": price.text.strip() if price else None,
    "description": description.text.strip() if description else None,
    "reviews": reviews.text.strip() if reviews else None,
    "rating": len(rating),
    "category": category.split("/")[-1]
}

                page_data.append(item)

            except Exception as e:
                logging.error(f"Product parsing error: {e}")

        return page_data

    except Exception as e:
        logging.error(f"Request failed: {e}")
        return []

def scrape_data():
    all_products = []

    for category in CATEGORIES:
        url = BASE_URL + category

        logging.info(f"Scraping {url}")

        data = scrape_page(url)

        all_products.extend(data)

        sleep(1)

    with open("data/raw_products.json", "w") as f:
        json.dump(all_products, f, indent=4)

    logging.info("Raw data saved")

    return all_products

if __name__ == "__main__":
    scrape_data()