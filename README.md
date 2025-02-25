# Web Scraping and Data Analysis Notebook

This Jupyter notebook demonstrates the process of web scraping, data cleaning, and basic data analysis using Python. The notebook focuses on analyzing product data scraped from an e-commerce website (Jumia) and provides insights into the price distribution of laptops.

## Table of Contents
1. [Introduction](#introduction)
2. [Libraries Used](#libraries-used)
3. [Data Loading](#data-loading)
4. [Data Cleaning](#data-cleaning)
5. [Basic Analysis](#basic-analysis)
6. [Most Expensive Products](#most-expensive-products)
7. [Price Distribution Visualization](#price-distribution-visualization)

## Introduction
This notebook performs the following tasks:
- Loads scraped product data from a CSV file.
- Cleans the price data by removing currency symbols and converting it to numeric values.
- Conducts basic statistical analysis on the price data.
- Identifies the top 5 most expensive products.
- Visualizes the price distribution of laptops using a histogram.

## Libraries Used
The notebook utilizes the following Python libraries:
- `pandas`: For data manipulation and analysis.
- `matplotlib`: For data visualization.

## Data Loading
The data is loaded from a CSV file named `jumia_products.csv`. This file contains product information, including product names, prices, and links.

```python
df = pd.read_csv("jumia_products.csv")

Analysis Report: https://docs.google.com/document/d/12ygggSTOL709JnasmGpW4fFFSk28mM7B6LQpvpn0Zd4/edit?tab=t.0

