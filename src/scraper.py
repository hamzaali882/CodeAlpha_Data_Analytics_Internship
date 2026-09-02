import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor

headers = {
    "User-Agent": "Mozilla/5.0"
}
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

def get_category(product_url):
    product_response = requests.get(product_url, headers=headers)
    product_response.encoding = "utf-8"
    product_response.raise_for_status()

    product_soup = BeautifulSoup(product_response.text, "html.parser")
    category = product_soup.select("ul.breadcrumb li a")[-1].get_text(strip=True)

    return category
books_data = []

for page in range(1, 51):
    url = base_url.format(page)

    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        product_url = urljoin(response.url, book.h3.a["href"])
        
        price = book.find("p", class_="price_color").text.strip()
        price = price.replace("Â£", "").replace("£", "")
        price = float(price)

        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        rating = book.find("p", class_="star-rating")["class"][1]

        books_data.append({
            "Title": title,
            "Product_URL": product_url,
            "Price_GBP": price,
            "Rating": rating,
            "Availability": availability
        })

product_urls = [book["Product_URL"] for book in books_data]

with ThreadPoolExecutor(max_workers=10) as executor:
    categories = list(executor.map(get_category, product_urls))

for book, category in zip(books_data, categories):
    book["Category"] = category
    
    
print("Total books scraped:", len(books_data))


df = pd.DataFrame(books_data)

df.to_csv(
    "data/books_dataset.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Dataset saved successfully!")