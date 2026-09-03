# CodeAlpha Data Analytics Internship

This repository contains the projects I completed during my Data Analytics
Internship at CodeAlpha.

The internship focuses on applying Python and data analytics concepts to
different real-world style projects.

## Internship Tasks

### Task 1 — Web Scraping

**Project:** E-Commerce Book Data Web Scraping using Python

For this task, I scraped book information from Books to Scrape using Python.

The dataset contains 1,000 books and includes information such as:

- Book title
- Product URL
- Price
- Rating
- Availability
- Category

**Tools used:**
- Python
- Requests
- BeautifulSoup
- Pandas

**Files:**
- `task1_web_scraping/data/books_dataset.csv`
- `task1_web_scraping/notebook/web_scraping.ipynb`
- `task1_web_scraping/src/scraper.py`

---

### Task 2 — Exploratory Data Analysis

**Project:** E-Commerce Book Dataset EDA

For this task, I explored the book dataset collected during Task 1.

The analysis included:

- Dataset overview
- Data types
- Missing value checking
- Duplicate checking
- Price analysis
- Rating analysis
- Category analysis
- Statistical summaries
- Basic visualizations

**Tools used:**
- Python
- Pandas
- Matplotlib

**File:**
- `task2_eda/eda_analysis.ipynb`

---

### Task 3 — Data Visualization

**Project:** E-Commerce Book Dataset Visualization

For this task, I created different visualizations to understand patterns
in book prices, ratings, and categories.

The visualizations included:

- Rating distribution
- Book price distribution
- Top book categories
- Average price by rating
- Average price by category
- Book price vs rating
- Price distribution by rating

**Tools used:**
- Python
- Pandas
- Matplotlib

**File:**
- `task3_data_visualization/data_visualization.ipynb`

---

### Task 4 — Sentiment Analysis

**Project:** Sentiment Analysis of Book Reviews

For this task, I analyzed a dataset containing 1,209 book reviews and
identified three sentiment categories:

- Positive
- Negative
- Neutral

The analysis included:

- Checking the dataset for missing values and duplicates
- Cleaning review text
- Converting sentiment labels into readable names
- Analyzing common words
- Comparing words across different sentiments
- Analyzing review length
- Visualizing sentiment distribution
- Calculating sentiment percentages

**Tools used:**
- Python
- Pandas
- Matplotlib
- Regular Expressions

**File:**
- `task4_sentiment_analysis/sentiment_analysis.ipynb`

---

## Repository Structure

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
├── task3_data_visualization/
│   └── data_visualization.ipynb
│
├── task4_sentiment_analysis/
│   ├── g_reviews.csv
│   └── sentiment_analysis.ipynb
│
├── requirements.txt
└── README.md