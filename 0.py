"""The hint is pretty informative for this problem; change the current number
in the url to the given number on the webpage, which is 2**38. Open the
new url and in the default browser."""
import webbrowser

webbrowser.open(f"http://www.pythonchallenge.com/pc/def/{2**38}.html")
