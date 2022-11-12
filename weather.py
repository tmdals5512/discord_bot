import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import unquote

year = str(datetime.today().year)
month = str(datetime.today().month)
day = str(datetime.today().day)
date = year + month + day

hour = str(datetime.today().hour)
minute = str(datetime.today().minute)
second = str(datetime.today().second)
basetime = hour + "00"
currenttime = hour + ":" + minute + ":" + second

y = '58'
x = '75'  #신창동 x,y 좌표

servicekey = ''
servicekey = unquote(servicekey)
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
params ={'serviceKey' : servicekey, 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'XML', 
        'base_date' : date, 'base_time' : basetime, 'nx' : x, 'ny' : y }

response = requests.get(url, params=params)
#print(url,params)
print(response.content)
