from bs4 import BeautifulSoup
import re
from random import shuffle

path = "quotes/70_historical_figures_indeed.html"
with open(path, encoding = "utf-8") as f:
	page = f.read()

soup = BeautifulSoup(page, "html.parser")

ls = list(soup.find("ol", class_ = "rich-text-component css-15dzfht eu4oa1w0"))
results = []

for elem in ls:
	x = re.sub("\n", "", elem.text)
	results.append(x)

shuffle(results)
for i in results:
	print(i)