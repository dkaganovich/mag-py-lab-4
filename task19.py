# import urllib2
import requests
from bs4 import BeautifulSoup

def extract_links(html_doc):
    soup = BeautifulSoup(html_doc, "html.parser")
    for link in soup.find_all("a"):
        yield link.get("href")

#html_doc = #requests.get("http://google.com").text#urllib2.urlopen("http://google.com").read()
html_doc = '<div id="mw-content-text"><p><a class="new" href="http://12">hello</a>Hoho()<a href="http://23">world</a>gpgp(<a href="http://34">jjj</a>)</p></div>'
for l in extract_links(html_doc):
    print l
