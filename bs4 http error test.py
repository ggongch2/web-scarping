from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import HTTPError 

try :
    html = urlopen('https://pythonscraping.com/pages/error.html')
except HTTPError as e :
    print(e)
else :
    print("continue")