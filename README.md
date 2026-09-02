# E-Commerce Book Data Web Scraping using Python

## Project Overview

This project demonstrates web scraping using Python. Book information was collected from the **Books to Scrape** website and organized into a structured dataset.

## Objective

The main goal of this project was to collect book data from all 50 pages of the website and prepare it for further analysis.

The following information was collected:

* Book title
* Price
* Rating
* Availability
* Product URL
* Category

## Tools and Libraries

* Python
* Requests
* BeautifulSoup
* Pandas
* Matplotlib

## Data Source

The data was collected from **Books to Scrape**, a website made for practicing web scraping.

Source: https://books.toscrape.com/

## Dataset

The final dataset contains:

* **1,000 books**
* **6 columns**
* **50 categories**
* No missing values
* No duplicate rows

The dataset is saved as:

`data/books_dataset.csv`

## Project Structure

```text
CodeAlpha_WebScraping/
│
├── data/
│   └── books_dataset.csv
│
├── notebook/
│   └── web_scraping.ipynb
│
├── src/
│   └── scraper.py
│
├── requirements.txt
└── README.md
```

## Key Findings

* The average book price is approximately **£35.07**.
* Book prices range from **£10.00 to £59.99**.
* All 1,000 books were listed as **In stock**.
* The dataset contains **50 different categories**.
* The most common rating is **One star**.

## Conclusion

This project helped me practice web scraping with Python and learn how to collect, organize, check, and visualize data from a website. The final dataset can also be used for further data analysis and visualization projects.
