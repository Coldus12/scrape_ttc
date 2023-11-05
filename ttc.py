from __future__ import print_function
import getopt, sys
import pickle
import time
from bs4 import BeautifulSoup
from selenium import webdriver

def get_listings_from_page(driver, url, nr, max_price=None):
    # Return list
    listings = []

    # Load webpage
    driver.get(url + "&page=" + str(nr))

    # Add cookies
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)

    # Wait 3 seconds for page to fully load
    time.sleep(1)

    # Get ready to parse page
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    table = soup.find("table", { "class" : "trade-list-table" })
    if type(table) is type(None):
        return listings

    table_findall = table.findAll("tr")
    if type(table_findall) is type(None):
        print("table was null")
        return listings

    for row in table_findall:
        if type(row) is type(None):
            print("Error: row is None")
            continue

        cells = row.findAll("td")

        listing_data = {}
        price = 9999999999

        for data in cells:
            if type(data) is type(None):
                continue

            guild_name_div = data.findAll("div", {"data-bind" : "text: GuildName"})
            player_id_div = data.findAll("div", {"data-bind" : "text: PlayerID"})
            
            location_a = data.findAll("a")
            
            amount_span = data.findAll("span", {"data-bind" : "localizedNumber: Amount"})
            unit_price_span = data.findAll("span", {"data-bind" : "localizedNumber: UnitPrice"})
            total_price_span = data.findAll("span", {"data-bind" : "localizedNumber: TotalPrice"})
            
            for g_name in guild_name_div:
                listing_data['guild_name'] = g_name.string
                
            for player_id in player_id_div:
                listing_data['player_id'] = player_id.string
            
            for location in location_a:
                listing_data['location'] = location.string
            
            for amount in amount_span:
                listing_data['amount'] = int(amount.string.replace(",","").split(".")[0])
            
            for unit_price in unit_price_span:
                price = int(unit_price.string.replace(",","").split(".")[0])
                listing_data['unit_price'] = price 
            
            for total_price in total_price_span:
                listing_data['total_price'] = int(total_price.string.replace(",","").split(".")[0])
            
            if type(data.string) is not type(None):
                if ("Now" in data.string) or ("minute" in data.string) or ("Minute" in data.string):
                    listing_data['last_seen'] = data.string

        if listing_data != {}:
            if max_price is None:
                listings.append(listing_data)
            else:
                if price < max_price:
                    listings.append(listing_data)

    return listings

def get_unit_price(listing):
    return listing.get('unit_price')

def main():
    all_listings = []

    url = ''
    pagenr = 5
    max_price = None

    argnr = len(sys.argv)

    if argnr > 1:
        url = str(sys.argv[1])
        if "http" not in url:
            url = "https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?ItemNamePattern=" + url + "&SortBy=LastSeen&Order=desc"
    else:
        print("No url/item name was provided, exiting script")
        return

    if argnr > 2:
        pagenr = int(sys.argv[2])

    if argnr > 3:
        max_price = int(sys.argv[3])

    option = webdriver.ChromeOptions()

    option.add_argument('--headless')
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-sh-usage')
    option.binary_location = '/usr/bin/chromium-browser'

    driver = webdriver.Chrome(options=option)

    for i in range(pagenr):
        all_listings.extend(get_listings_from_page(driver, url, i, max_price=max_price))

    driver.quit()

    all_listings.sort(key=get_unit_price)

    print(*all_listings, sep='\n')


if __name__ == "__main__":
    main()
