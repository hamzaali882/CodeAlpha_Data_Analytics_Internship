# CodeAlpha Internship — Data Analytics Projects

## Task 1: Web Scraping

### E-Commerce Book Data Web Scraping using Python

### Project Overview

This project demonstrates web scraping using Python. Book information was collected from the **Books to Scrape** website and organized into a structured dataset.

### Objective

The main goal of this project was to collect book data from all 50 pages of the website and prepare it for further analysis.

The following information was collected:

* Book title
* Price
* Rating
* Availability
* Product URL
* Category

### Tools and Libraries

* Python
* Requests
* BeautifulSoup
* Pandas
* Matplotlib

### Data Source

The data was collected from **Books to Scrape**, a website made for practicing web scraping.

Source: https://books.toscrape.com/

### Dataset

The final dataset contains:

* **1,000 books**
* **6 columns**
* **50 categories**
* No missing values
* No duplicate rows

The dataset is saved inside the Task 1 folder.

### Task 1 Project Structure

```text
task1_web_scraping/
├── data/
│   └── books_dataset.csv
├── notebook/
│   └── web_scraping.ipynb
└── src/
    └── scraper.py
```

### Key Findings

* The average book price is approximately **£35.07**.
* Book prices range from **£10.00 to £59.99**.
* All 1,000 books were listed as **In stock**.
* The dataset contains **50 different categories**.
* The most common rating is **One star**.

### Task 1 Conclusion

This project helped me practice web scraping with Python and learn how to collect, organize, check, and visualize data from a website. The final dataset can also be used for further data analysis and visualization projects.

---

# Task 2: Exploratory Data Analysis

## E-Commerce Book Dataset EDA

### Project Overview

In Task 2, I explored the book dataset collected during Task 1. The goal was to understand the data, identify patterns, and find useful insights about book prices, ratings, categories, and availability.

### Objective

The main objectives of this analysis were:

* Understand the structure of the dataset
* Check for missing values and duplicate rows
* Analyze book prices
* Explore book ratings
* Explore book categories
* Compare prices across ratings and categories
* Find useful patterns and insights

### Analysis Performed

The following analysis was performed using Python:

* Dataset overview
* Data type checking
* Missing value checking
* Duplicate checking
* Price statistics
* Rating distribution
* Category distribution
* Cheapest and most expensive books
* Average price by rating
* Average price by category
* Availability analysis
* Price distribution visualization

### Key Findings

* The dataset contains **1,000 books** and **6 columns**.
* There are **no missing values**.
* There are **no duplicate rows**.
* The average book price is around **£35.07**.
* Book prices range from **£10.00 to £59.99**.
* There are **50 different categories**.
* **Default** is the most common category, with 152 books.
* **One-star** books are the most common rating, with 226 books.
* All 1,000 books are listed as **In stock**.
* Average book prices vary across different ratings and categories.

### Task 2 Project Structure

```text
task2_eda/
└── eda_analysis.ipynb
```

### Task 2 Conclusion

In this task, I explored the book dataset collected during Task 1 and analyzed its main characteristics. I checked the data quality and explored prices, ratings, categories, and availability.

This task gave me more practice with Pandas, basic data analysis, and data visualization using Python. It also helped me understand how exploratory data analysis can be used to find useful patterns in a dataset.

---

## Overall Project Structure

```text
CodeAlpha_WebScraping/
│
├── task1_web_scraping/
│   ├── data/
│   │   └── books_dataset.csv
│   ├── notebook/
│   │   └── web_scraping.ipynb
│   └── src/
│       └── scraper.py
│
├── task2_eda/
│   └── eda_analysis.ipynb
│
├── requirements.txt
└── README.md
```

## Internship Progress

* [x] Task 1 — Web Scraping
* [x] Task 2 — Exploratory Data Analysis
* [ ] Task 3 — Data Visualization
* [ ] Task 4 — Sentiment Analysis
