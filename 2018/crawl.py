from bs4 import BeautifulSoup
import urllib2


query = "sherlock"

url = "https://www.imdb.com/find?ref_=nv_sr_fn&q=" + query + "&s=all"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content, "html.parser")

results = soup.findAll("tr", {"class": "findResult"})

for result in results:
    print "https://www.imdb.com" + result.find("td", {"class": "result_text"}).a.get("href")