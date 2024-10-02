import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://store.steampowered.com/search/?specials=1&os=win'

response = requests.get(url)

if response.status_code == 200:
    
    soup = BeautifulSoup(response.content, 'html.parser')

    games = soup.find_all('a', class_='search_result_row', limit=15)

    game_data = []

    for game in games:
        
        data_discounts = game.find('div', class_='discount_pct')  
        data_finalprice = game.find('div', class_='discount_final_price')
        data_body = game.find('span', class_='title')
        
        data_ratings = game.find('span', class_='search_review_summary')
        rating = data_ratings['data-tooltip-html'] if data_ratings else None

        game_data.append({
            'Game Name': data_body.text if data_body else None,
            'Price': data_finalprice.text if data_finalprice else None,
            'Discount (%)': data_discounts.text if data_discounts else None,
            'Rating': rating if rating else 'No Rating'
        })

    for game in game_data:
        print(f"Game Name: {game['Game Name']}")
        print(f"Price: {game['Price']}")
        print(f"Discount (%): {game['Discount (%)']}")
        print(f"Rating: {game['Rating']}\n")

    df = pd.DataFrame(game_data)
    df.to_excel('steam_scraping.xlsx', index=False)

    print("Data saved to steam_scraping.xlsx")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
