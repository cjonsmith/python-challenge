"""The first hint for this problem is the title of the webpage: 'peak hell'.
When pronounced, it sounds very similar to 'pickle', which is the builtin
python object serialization package. When viewing the the source code of the
webpage, there is a 'peakhell' tag that links to a pickle file. We'll download
the file (prompting the user if they are okay with deserializing the file) then
view its contents."""
import pickle
import requests
import webbrowser
from bs4 import BeautifulSoup

webpage = "http://www.pythonchallenge.com/pc/def/peak.html"
r = requests.get(webpage)
soup = BeautifulSoup(r.content, "html.parser")

peakhell = soup.find("peakhell")["src"]

split_page = webpage.split("peak.html")
pickle_file = f"{split_page[0]}{peakhell}"

r = requests.get(pickle_file)
with open(peakhell, "wb") as fp:
    fp.write(r.content)

# Print out each line to the console.
msg = pickle.load(open(peakhell, "rb"))
line = ""
for lst in msg:
    for tup in lst:
        line += tup[0] * tup[1]
    print(line)
    line = ""

print("opening new webpage...")
split_page = webpage.split("peak.html")
new_page = f"{split_page[0]}channel.html"
webbrowser.open(new_page)
