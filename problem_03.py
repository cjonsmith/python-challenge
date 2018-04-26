"""Similar to the last problem, the bulk of 3.py is scraping a large comment
from the source of the webpage in order to find the name of the next webpage
to visit. The hint this time is to look for one "small letter" surrounded
by exactly three "big bodyguards" (letters) on each of its sides. To find all
matches of this pattern, construct a regular expression that will match to
exactly three uppercase letters, a single lowercase letter, and an additional
three uppercase letters. We'll preserve the named group for the lowercase
letters then join them together to get the name of the next webpage."""
import re
import requests
import webbrowser
from bs4 import BeautifulSoup, Comment

# Construct the regular expression.
# Ensure that there are only three capiltal letters surrounding the lowercase
# letter on either side; no more, no less.
regex = "[^A-Z][A-Z]{3}(?P<letter>[a-z])[A-Z]{3}[^A-Z]"

# Send a get request to the webpage and construct a parse tree from its content.
webpage = "http://www.pythonchallenge.com/pc/def/equality.html" 
r = requests.get(webpage)
soup = BeautifulSoup(r.content, "html.parser")

# Find the mess of characters to search.
chars = soup.find(string=lambda text: isinstance(text, Comment))

# Find all matches within the characters. re.findall returns a list containing
# all of the contents of each named group in order of appearance; join this 
# list together to construct the name of the next webpage.
msg = "".join(re.findall(regex, chars))
print(msg)

# When viewing the new webpage, it informs us that the file is no longer an
# html file, but a php file. Change the destination webpage accordingly.
split_page = webpage.split("equality")
split_page[1] = split_page[1].replace("html", "php")
webbrowser.open(split_page[0] + msg + split_page[1])
