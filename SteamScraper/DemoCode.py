import requests
import bs4 as BeautifulSoup

#opening a connection 
url = 'https://store.steampowered.com/search/?specials=1&os=win'

response = requests.get(url)

if response.status_code == 200:

    #turning the html into a beautifulsoup object
    soup = BeautifulSoup(response.content, 'html.parser')

    games = soup.find_all('a', class_='search_result_row', limit=15)

    game_data = []  

    for game in games:

        data_discounts = (soup.find_all('div', {'class':'discount_pct'}))
        data_finalprice = (soup.find_all('div', {'class':'discount_final_price'}))
        data_body = (soup.find_all('span', {'class':'title'}))

        game_data.append({
            'Game Name': data_body,
            'Price': data_finalprice,
           # 'Discount (%)': discount_numeric,
            # 'Rating': rating
        })
    print (game_data)
