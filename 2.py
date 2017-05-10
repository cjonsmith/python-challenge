"""The hint for this problem directs us to the page source, which contains
a very large comment with a note saying "find rare characters". Send a get
request to the page and construct a BeautifulSoup parser to find the second
comment (the one with mess of characters) then use a dictionary to keep count
of all the characters. Then find the keys with the smallest value associated
with them.

Once we have a dictionary of the characters and the number of times they appear,
we can sort them based on their values and view the results. We'll notice that
the first eight characters in acending order of appearence will spell 
'equality'. We'll use this as the name of the next riddle's page.
"""
import requests
import webbrowser
from bs4 import BeautifulSoup, Comment

# Send the request and build the parse tree.
webpage = "http://www.pythonchallenge.com/pc/def/ocr.html"
r = requests.get(webpage)
soup = BeautifulSoup(r.content, "html.parser") # lmxl parser wouldn't find all
                                               # comments.

# Find the second comment.
chars = soup.find_all(string=lambda text:isinstance(text, Comment))[1]

# Map each character to a count of how many times it appears.
counts = {}
for ch in chars:
    if ch not in counts:
        counts[ch] = 0
    counts[ch] += 1

# Print the characters in order of least ocurrences.
# We'll notice that the first eight letters spell equality.
ordered = sorted(counts, key=lambda x:counts[x])
msg = "".join(ordered[:9])
print(msg)

# Lets open a new page who's name is the contents of the secret message.
split_page = webpage.split("ocr")
webbrowser.open(split_page[0] + msg + split_page[1])
