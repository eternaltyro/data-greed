#!/usr/bin/python
import json
from BeautifulSoup import BeautifulSoup, NavigableString
import requests

baseurl = 'http://www.projectmadurai.org'
scrapeurl = baseurl + '/pmworks.html'
page = requests.get(scrapeurl).content
soup = BeautifulSoup(page)
table = soup.find('table', { 'id': 'sortabletable'})
dd = [ch for ch in table.childGenerator()]

body = dd[1]
#children = body.childGenerator
dd = [ch for ch in body.childGenerator()]

data = dict()
row = 0
for ch in dd:
	if not isinstance(ch , NavigableString):
		childGen = ch.childGenerator()
		count =0
		data["row %s" % row] = {}
		for child in childGen:
			print type(child)
			if not isinstance(child , NavigableString):
				data["row %s" % row]["column %s" % count] = child.text
			else:
				data["row %s" % row]["column %s" % count] = child.title()
			count += 1
		row +=1

txxt = json.dumps(data, ensure_ascii=False, indent=4)
ff = open("test.json", "w")
#This is used to spacify encodeing type of this content.
ff.write(u'\ufeff'.encode("utf-8"))
ff.write(txxt.encode("utf-8"))
ff.close()
