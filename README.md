# Python Steam Sale Scraper

This repository contains a simple Python script that scrapes Steam's sale page for games on discount and saves the results into an Excel file. This tool is helpful for tracking game deals and finding the best discounts.
Prerequisites

## To use this project, ensure you have the following:

    Python 3.6 or higher
    You can download it from Python’s official website.

    pip
    Pip is the package installer for Python, included by default with Python 3 installations. Update it to the latest version with:

pip install --upgrade pip

Required Libraries
This project uses:

    requests – For sending HTTP requests to Steam.
    BeautifulSoup (part of the bs4 library) – For parsing HTML.
    pandas – For managing and exporting data.

Install these libraries using:

    pip install requests beautifulsoup4 pandas

## How It Works

The Steam Sale Scraper sends a request to the Steam specials page, parses the HTML response to extract details such as game name, discount, final price, and rating, and then saves the extracted information into an Excel file.
Setup and Usage
1. Clone the Repository

Start by cloning this repository:

git clone https://github.com/LibmusHawk/python-steam-scraper.git
cd steam-sale-scraper

2. Run the Script

To run the scraper, execute:

python steam_sale_scraper.py

The script will scrape data from the Steam sales page and save the results to steam_scraping.xlsx in the same directory.
Code Overview

Here is the code for steam_sale_scraper.py:

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://store.steampowered.com/search/?specials=1&os=win'

# Send request to the Steam sale page
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all games on sale (limit to first 15 results)
    games = soup.find_all('a', class_='search_result_row', limit=15)
    game_data = []
    
    # Extract game information
    for game in games:
        data_discounts = game.find('div', class_='discount_pct')  
        data_finalprice = game.find('div', class_='discount_final_price')
        data_body = game.find('span', class_='title')
        
        # Game rating (if available)
        data_ratings = game.find('span', class_='search_review_summary')
        rating = data_ratings['data-tooltip-html'] if data_ratings else None

        game_data.append({
            'Game Name': data_body.text if data_body else None,
            'Price': data_finalprice.text if data_finalprice else None,
            'Discount (%)': data_discounts.text if data_discounts else None,
            'Rating': rating if rating else 'No Rating'
        })

    # Print each game’s details
    for game in game_data:
        print(f"Game Name: {game['Game Name']}")
        print(f"Price: {game['Price']}")
        print(f"Discount (%): {game['Discount (%)']}")
        print(f"Rating: {game['Rating']}\n")

    # Save data to Excel
    df = pd.DataFrame(game_data)
    df.to_excel('steam_scraping.xlsx', index=False)
    print("Data saved to steam_scraping.xlsx")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

## Code Explanation

    Requests: The script uses the requests library to fetch the HTML content of the Steam sale page.
    BeautifulSoup: Parses the HTML and extracts sale information for each game, including the game title, discount, price, and rating.
    Pandas: Stores the extracted data in a DataFrame and saves it to an Excel file.

## Example Output

Once you run the script, you’ll see output similar to the following in your console:

Game Name: Game 1
Price: $9.99
Discount (%): -50%
Rating: Mostly Positive

Game Name: Game 2
Price: $6.99
Discount (%): -30%
Rating: Very Positive
...
Data saved to steam_scraping.xlsx

The Excel file (steam_scraping.xlsx) will contain the following columns:

    Game Name
    Price
    Discount (%)
    Rating

## Troubleshooting

    HTTP Status Errors: If you encounter errors (e.g., Status code: 404), ensure the URL is correct and Steam's server is accessible.
    Data Not Found: If the Excel file doesn’t contain expected data, Steam may have updated its page structure. Inspect the page's HTML to adjust the scraping logic.
    Missing Libraries: Ensure requests, beautifulsoup4, and pandas are installed.
