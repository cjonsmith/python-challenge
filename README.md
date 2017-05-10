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
