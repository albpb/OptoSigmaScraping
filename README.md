# OptoSigma Scraping

Welcome to **OptoSigma Scraping**, a Python project that extracts product information from the OptoSigma website and formats it into a simple, organized JSON file. This project demonstrates web scraping using **BeautifulSoup** and data cleaning using **REGEX**.

## 📋 Overview

This program automates the process of collecting and cleaning product data from the OptoSigma website. It consists of two main scripts:
1. **`scrape.py`** - Scrapes product data from the website and stores it as raw JSON.
2. **`clean.py`** - Cleans and processes the scraped data for better readability and accuracy.

## 🛠️ Scripts

### `scrape.py`

This script is responsible for:
- Extracting product links from the OptoSigma website using **BeautifulSoup**.
- Navigating through each product link and parsing product information from the characteristics tables.
- Storing the parsed data in a dictionary format.
- Exporting the dictionary to a JSON file.

### `clean.py`

This script is used to clean up the raw product data collected from the OptoSigma website. The goal is to make the data more consistent, readable, and useful for further analysis or usage. The cleaning process involves the following steps:

- **Filter Important Properties**: It reduces the list of characteristics to only the most relevant product features.
- **Fix Formatting Errors**: Using **REGEX**, it corrects issues such as:
  - Improper spacing (e.g., `5mm` is converted to `5 mm`).
  - Correcting abbreviations or typos in units and symbols.
  - Removing any redundant information or symbols that might have been captured during scraping.
- **Table Output**: The cleaned data is formatted into a readable table for inspection.
- **Save Clean Data**: The final step is to save the processed data back into a JSON file.
