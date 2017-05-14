"""The image on the webpage is an anchor to another webpage with a similar
url. Appended to the end of the url however is a web-query entitled "nothing"
with a value of 44827. The content of the new page is "and the next nothing is",
followed by a number. This hints that we should alter the web-query by changing
the value of the webquery to the number found on the content of this page. 

Another hint is provided in the source code of the original page informing us
that we need not go past 400 new pages. The pattern described above will repeat
until a special webpage is found containing the name of the next page."""
import sys
import requests
import webbrowser
from bs4 import BeautifulSoup

webpage = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
r = requests.get(webpage)
soup = BeautifulSoup(r.content, "html.parser")

next_page = "http://www.pythonchallenge.com/pc/def/" + soup.find("a")["href"]
r = requests.get(next_page)
soup = BeautifulSoup(r.content, "html.parser")
print("This may take a while...")
num_scraped = 1
while True:
    sys.stdout.write(f"\rOn page {num_scraped}")
    sys.stdout.flush()
    if ".html" in soup.text:
        break
    if "Divide by two" in soup.text:
        num /= 2
    else:
        num = int(soup.text.split()[-1])
    next_page = "http://www.pythonchallenge.com/pc/def/linkedlist.php" \
                f"?nothing={num}"
    r = requests.get(next_page)
    soup = BeautifulSoup(r.content, "html.parser")
    num_scraped += 1

split_page = webpage.split("linkedlist.php")
new_page = f"{split_page[0]}{soup.text}"
webbrowser.open(new_page)
