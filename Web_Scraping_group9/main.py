import requests
from bs4 import BeautifulSoup
import csv

# Define the Jumia URL (Searching for "laptop")
URL = "https://www.jumia.com.ng/catalog/?q=laptop"

# Headers to mimic a real browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send a request to the website
response = requests.get(URL, headers=HEADERS)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")

    # Find product containers using the class name
    products = soup.find_all("article", class_="prd _fb col c-prd")

    data = []
    
    # Loop through each product and extract the title, price, and link
    for product in products:
        title_tag = product.find("h3", class_="name")
        price_tag = product.find("div", class_="prc")
        link_tag = product.find("a", class_="core")

        if title_tag and price_tag and link_tag:
            title = title_tag.text.strip()
            price = price_tag.text.strip()
            link = "https://www.jumia.com.ng" + link_tag["href"]
            data.append([title, price, link])

    # Save data to CSV
    with open("jumia_products.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Price", "Link"])
        writer.writerows(data)

    # check is the saving is successful
    print("Data successfully scraped and saved to jumia_products.csv")

else:
    # Print an error message if the request was not successful
    print("Failed to fetch the webpage. Status code:", response.status_code)