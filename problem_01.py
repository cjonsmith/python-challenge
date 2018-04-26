"""Caesar cipher where the given image is the key to the cipher:
K -> M (shift two positions right)
O -> Q (shift two positions right)
E -> G (shift two positions right)
The everybody thinks "twice" part is also hinting to the fact that we should 
shift all letters in the jumbled text below to the right.

Create a parsetree using BeautifulSoup to find the encrypted text, then using 
the key to the cipher, decrypt the message.

Once the message is decrypted, it tells us to decrypt the url. Decrypt the name
of the html file and use that as the name of the next html page.
"""
import requests
import webbrowser
from bs4 import BeautifulSoup
from string import ascii_lowercase

# Construct key to cipher by rotating the lowercase alphabet right by 2.
rot2 = ascii_lowercase[2:] + ascii_lowercase[:2]
key = str.maketrans(ascii_lowercase, rot2)

# Scrape the website to get the encrypted message.
webpage = "http://www.pythonchallenge.com/pc/def/map.html"
r = requests.get(webpage)
soup = BeautifulSoup(r.content, "lxml")
data = soup.find("td").get_text().strip().split("\n")
msg = data[-1]

# Use the translate function and the table constructed from str.maketrans to
# decode the message.
print(msg.translate(key))

# Now we know to decode the url too! We'll just decrypt the last part of the
# url, since that's how the problem worked on the last page.
split_page = webpage.split("map")
new_page = split_page[0] + "map".translate(key) + split_page[1]
print(new_page)

# Open the new webpage in the default web browser.
webbrowser.open(new_page)
