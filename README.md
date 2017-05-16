# python-challenge
My solutions to the "Python Challenge" online programming riddles: http://www.pythonchallenge.com/

## Solutions
<details>
<summary><strong>Problem 0</strong></summary>
The hint is pretty informative for this problem; change the current number
in the url to the given number on the webpage, which is 2<sup>38</sup>. 
Open the new url in the default browser.
</details>

<details>
<summary><strong>Problem 1</strong></summary>
Caesar cipher where the given image is the key to the cipher:</br>
K -> M (shift two positions right)</br>
O -> Q (shift two positions right)</br>
E -> G (shift two positions right)</br>

The everybody thinks "twice" part is also hinting to the fact that we should
shift all letters in the jumbled text below to the right.</br>

Create a parsetree using BeautifulSoup to find the encrypted text, then using 
the key to the cipher, decrypt the message.</br>

Once the message is decrypted, it tells us to decrypt the url. Decrypt the name
of the html file and use that as the name of the next html page.
</details>

<details>
<summary><strong>Problem 2</strong></summary>
The hint for this problem directs us to the page source, which contains
a very large comment with a note saying "find rare characters". Send a get
request to the page and construct a BeautifulSoup parser to find the second
comment (the one with mess of characters) then use a dictionary to keep count
of all the characters. Then find the keys with the smallest value associated
with them.</br>

Once we have a dictionary of the characters and the number of times they appear,
we can sort them based on their values and view the results. We'll notice that
the first eight characters in acending order of appearence will spell 
'equality'. We'll use this as the name of the next riddle's page.
</details>

<details>
<summary><strong>Problem 3</strong></summary>
Similar to the last problem, the bulk of 3.py is scraping a large comment
from the source of the webpage in order to find the name of the next webpage
to visit. The hint this time is to look for one "small letter" surrounded
by exactly three "big bodyguards" (letters) on each of its sides. To find all
matches of this pattern, construct a regular expression that will match to
exactly three uppercase letters, a single lowercase letter, and an additional
three uppercase letters. We'll preserve the named group for the lowercase
letters then join them together to get the name of the next webpage.
</details>

<details>
<summary><strong>Problem 4</strong></summary>
The image on the webpage is an anchor to another webpage with a similar
url. Appended to the end of the url however is a web-query entitled "nothing"
with a value of 44827. The content of the new page is "and the next nothing is",
followed by a number. This hints that we should alter the web-query by changing
the value of the webquery to the number found on the content of this page. 

Another hint is provided in the source code of the original page informing us
that we need not go past 400 new pages. The pattern described above will repeat
until a special webpage is found containing the name of the next page.
</details>
