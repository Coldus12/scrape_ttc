# TTC scraper
This is a simple python script with the goal of getting ESO guild store item data from tamrieltradecentre.com.
The main feature of this script is to show the newly listed items, sorted by price. This enables finding items listed recently (which presumably haven't been bought yet), with (hopefully) low prices. 
# Requirements
The script uses the selenium, beautifulsoup4, and pickle libraries / packages.
Selenium itself requires a chrome/chromium installation as well as a chrome/chromium-driver.
The installation of these packages / software is out of scope of this script, and its README.
# Usage
TTC uses captcha, so it is recommended to first run save_cookies.py via

    python3 save_cookies.py
A browser will open with TTC, and you have to load the page. Most probably it won't ask you to do a captcha, but if it does you should do it. The save_cookies.py script leaves you 60 seconds to finish the captcha. The cookies are saved via pickle.

After this you can now run the ttc.py itself:

    python3 ttc.py item+name [numberOfPages] [max_price]
The item+name can be the name of the item you desire to buy, with spaces swapped to plus signs, for example "Dreugh Wax" should be input as "Dreugh+Wax".
### Example usage

    python3 ttc.py Dreugh+Wax 20 20000
### Arguments
The arguments in [] are optional parameters. The default number of pages is 5. 
If the max_price variable isn't set, then all items will be listed ordered by the item's unit_price.
Instead of inputting the name of the item you can also input a valid ttc url as well such as:

    python3 ttc.py 'https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?ItemID=5687&SortBy=LastSeen&Order=desc'
### Notes for windows users
Both `ttc.py` and `save_cookies.py` are configured to use a chromium driver from /usr/bin/chromium-browser, to use the default chromedriver location just uncomment the line
" `options.binary_location = '/usr/bin/chromium-browser'` "
or change the location to the correct one.

### Example output
The output is json like: (Can easily be converted to json if needed)

{'player_id': '@Handwerksmeister', 'guild_name': 'Dark Shadow Trading', 'location': 'Vvardenfell: Vivec City', 'amount': 2, 'unit_price': 60000, 'total_price': 120000, 'last_seen': 'Now'}

{'player_id': '@Handwerksmeister', 'guild_name': 'Dark Shadow Trading', 'location': 'Vvardenfell: Vivec City', 'amount': 2, 'unit_price': 60000, 'total_price': 120000, 'last_seen': 'Now'}

{'player_id': '@Handwerksmeister', 'guild_name': 'Dark Shadow Trading', 'location': 'Vvardenfell: Vivec City', 'amount': 2, 'unit_price': 60000, 'total_price': 120000, 'last_seen': 'Now'}
