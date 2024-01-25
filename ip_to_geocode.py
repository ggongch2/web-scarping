import json
from urllib.request import urlopen

def getCountry(ipAddress) :
    response = urlopen("http://ip-api.com/json/"+ipAddress).read()
    responseJson = json.loads(response)
    #print(responseJson) 
    return responseJson.get("countryCode")

ipAdd = "59.9.127.16"
# decode('utf-8')
print("ip주소의 국가코드 :", getCountry(ipAdd))