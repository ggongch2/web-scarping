import json
from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag
from urllib.request import HTTPError 
import re 
import random
import sys



# 초기문서 -> 초기 문서에 있는 모든 링크 수집 -> 하나하나마다 문서의 편집자의 국가, 지역을 조사함(사진일경우 제외) -> link가 빌때까지 반복 

def getCountry(ipAddress, type) :
    response = urlopen("http://ip-api.com/json/"+ipAddress).read()
    responseJson = json.loads(response)
    #print(responseJson) 
    if type == "Country" : 
        return responseJson.get("country")
    elif type == "Region" : 
        region = responseJson.get("regionName") + " "+ responseJson.get("city")
        return region
 
def getlinks(url) :
      html = urlopen(url) 
      bsObj = BeautifulSoup(html, "html.parser")
      link_compliation = set()
      link = bsObj.find('div', id ="bodyContent").find_all('a')      
      pattern = re.compile('https://en\.wikipedia\.org/wiki/.*') # en 기준
      for each in link :
        if 'href' in each.attrs :
            link_text = each.get("href")
            if pattern.match(link_text) :
                link_compliation.add("https://en.wikipedia.org"+link_text) # 위키인지 검사하는거 해야함  --> 아직
      return list(link_compliation)

def historyIPs(url) :
    print("------------------------------------------------------------------------------")
    title_name = (url.split('/'))[-1]
    history_url = "https://en.wikipedia.org/w/index.php?title=" + title_name + "&action=history" # 영어위키백과 기준
    print("문서 제목 :", title_name, "url : ", url) 
    html = urlopen(history_url) 
    bsObj = BeautifulSoup(html, "html.parser") 

    ip_compliation = set()
    ipS = bsObj.find_all(class_ = 'mw-userlink mw-anonuserlink')

    for each in ipS :
        ip_compliation.add(each.text)

    if(len(ip_compliation) == 0) :
        print("ip X ")

    for each in list(ip_compliation) :
        print(getCountry(each, "Country")) 
    print("------------------------------------------------------------------------------")
    


count = 0 
links = getlinks("https://en.wikipedia.org/wiki/Cristiano_Ronaldo")

while len(links) > 0 and count <= 100 :
    for each in links : 
        historyIPs(each) 
    count += 1
    links = links[random.randrange(0, len(links))]
    print("________________________________________________________________________")
    for each in links :
        print(each) 
    print("________________________________________________________________________")


#https://en.wikipedia.org/wiki/Goguryeo
#https://en.wikipedia.org/w/index.php?title=Goguryeo&action=history

#위키 주소인지 검사해야함 - 템플릿 같은거나 이미지 주소 
#404면 넘어가 -> 아직 
#ip쓰는 사람이 없으면 출력 x? 
    # https://en.wikipedia.org#cite_ref-36
    # https://en.wikipedia.org/wiki/2016%E2%80%9317_UEFA_Champions_League







