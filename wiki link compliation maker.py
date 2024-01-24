from bs4 import BeautifulSoup, Tag
from urllib.request import urlopen
from urllib.request import HTTPError 
import re 

url = "https://ko.wikipedia.org/wiki/%EC%A7%80%EC%A7%84"
html = urlopen(url) 
bsObj = BeautifulSoup(html, "html.parser")


link_compliation = [] 
pattern = re.compile('/wiki/')
link = bsObj.find('div', id ="bodyContent").find_all('a')

f= open("link_comp.txt", 'w', encoding = 'utf-8') 


for each in link :
	if 'href' in each.attrs :
		link_text = each.get("href")
		link_name = each.get("title") 
		if pattern.match(link_text) :
			link_compliation.append({link_name, link_text}) 
			content = str(link_name) + " : " + str(link_text) + '\n'
			f.write(content)  

							 
print(link_compliation) 

	#<a href="/wiki/%EC%A7%80%EC%A7%84%ED%8C%8C" title="지진파">지진파</a>