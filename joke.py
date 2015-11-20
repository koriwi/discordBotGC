from lxml import html
from lxml.cssselect import CSSSelector
import requests
import random


def getJoke():

    print("A user requested a joke")
    url = "http://1a-flachwitze.de/beste/page/"
    random.seed()
    number = random.randrange(1, 72, 1)
    number1 = random.randrange(0, 3, 1)
    url = url +str(number)
    print("Url:"+url)
    print("Page:"+str(number))
    print("Joke:"+str(number1))
    page = requests.get(url)
    tree=html.fromstring(page.content)
    text1 = tree.cssselect('.post > header > h2 > a')
    text2 = tree.cssselect('.post > div > p')
    print("Found "+str(len(text1))+" jokes")
    quest=text1[number1].text.encode('utf-8').strip()
    pointe=text2[number1].text.encode('utf-8').strip()

    print("Joke: "+quest)
    print("Pointe: "+pointe)

    return quest+"\n"+pointe
