from bs4 import BeautifulSoup
import re
from random import shuffle

path = "quotes/101_quotes_inc.html"
with open(path, encoding = "utf-8") as f:
	page = f.read()

soup = BeautifulSoup(page, "html.parser")

ls = list(soup.find_all("p"))
res = []
for i in ls:
	i = re.sub("\n", "", i.text.strip())
	m = re.match("\d+\. \"(.*)\"\s*\-+\s*(.*)", i)
	if m:
		res.append(f"'{m.group(1)}' - {m.group(2)}")

shuffle(res)
for i in res:
	print(i)