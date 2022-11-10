import random
import requests
from bs4 import BeautifulSoup

opgg = 'https://www.op.gg/summoners/kr/'

def get_response(message: str) -> str:
    if message[0:2] == '~~':
        message = message[2:]
        p_message = message.lower()

        if p_message == 'hello':
            return 'Hey there!'

        if message == 'roll':
            return str(random.randint(1, 12))
        
        if message == '잰추':
            return '쀽쀽!'
        
        if message.split(' ', 2)[0] == '롤전적검색' :
            url = opgg + (message.split(' ', 2)[1])
            #print(url)
            res = requests.get(url).text
            soup = BeautifulSoup(res, "html.parser")
            tiername = soup.find(class_ = "tier")
            print(tiername)           
            return (tiername)
    print("Empty returned")
    return