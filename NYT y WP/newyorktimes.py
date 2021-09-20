import requests
import re
from bs4 import BeautifulSoup

url="https://www.nytimes.com/"
r=requests.get(url)
html=r.text

scripts = re.compile(r'<(script).*?</\1>(?s)')
css = re.compile(r'<(style).*?</\1>(?s)')
#tags = re.compile(r'<.*?>(?s)')

text = scripts.sub(' ', html)
text = css.sub(' ', text)
#text = tags.sub(' ', text)

text1 = text.lower()
#for ch in ['/', '(', ')', '“', '”', ':', '«', '¿', '?', '»', '&', '. ', ', ', ';', '@', '©']:
#    if ch in text1:
#        text1=text1.replace(ch," ")


#list1 = text1.split( )
#my_dict = {i:list1.count(i) for i in list1}

#print(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))

##  lista title ##
soup = BeautifulSoup(text1, 'html.parser')

## TITLES

title = soup.find_all(class_='css-1cmu9py e1voiwgp0')
title1 = soup.find_all(class_='css-z9cw67 e1voiwgp0')
title4 = soup.find_all(class_='css-1yxu27x e1voiwgp0')
t1= []

for titles in title:
    t1.append(titles.contents[0])

for titles in title1:
    t1.append(titles.contents[0])

for titles in title4:
    t1.append(titles.contents[0])

title2 = soup.find_all('h2')

for titles in title2:
    title3 = titles.find_all('span')
    for x in title3:
        t1.append(x.contents[0])
print(t1)

print(len(t1))
## FIN TITLES

## COPETE

copete1 = soup.find_all(class_='css-1pfq5u e1lfvv700')
c1= []
for copete in copete1:
    c1.append(copete.contents[0])

copete2 = soup.find_all(class_='css-ip5ca7 e1lfvv701')

for copete in copete2:
    copete3 = copete.find_all('li')
    for c in copete3:
        c1.append(c.contents[0])
print(c1)

print(len(c1))

## FIN COPETE

## LINKS

link2 = soup.find_all(class_='css-6p6lnl')
link5 = soup.find_all(class_='css-qvz0vj eqveam61')
l1=[]

comment=re.compile(r'.+commentscontainer')
twitter=re.compile(r'.+twitter.+')

for link in link2:
    link3 = link.find_all('a')
    for l in link3:
        link4 = 'https://www.nytimes.com' + l.get('href')
        l1.append(link4)

for link in link5:
    link6 = link.find_all('a')
    for l in link6:
        link7 = 'https://www.nytimes.com' + l.get('href')
        l1.append(link7)

## lo que sigue es para borrar los href que llevan a la pagina de los comentarios, y un link a twitter que no se como sacarlo...

for x in l1:
    if re.match(comment, x) is not None:
        l1.remove(x)

for x in l1:
    if re.match(twitter, x) is not None:
        l1.remove(x)

print(l1)
print(len(l1))
## FIN LINKS


