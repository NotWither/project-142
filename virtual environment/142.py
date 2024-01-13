from bs4 import BeautifulSoup as bs
import requests 
import pandas as pd 
StarUrl = "https://en.wikipedia.org/wiki/List_of_nearest_giant_stars"

page=requests.get(StarUrl)
soup = bs(page.text,"html.parser")
startable=soup.find('table')
templist=[]
tablerows=startable.find_all('tr')
for  tr in tablerows:
    td=tr.find_all('td')
    row=[i.text.rstrip()for i in td]

    templist.append(row)
    print (templist)
starsname=[]
distance=[]
mass=[]
radius=[]    
for i in  range (1,len(templist)):
    starsname.append(templist [i][1])
    distance.append(templist [i][6])
    mass.append(templist [i][9])
    radius.append(templist [i][10])
headers=["starsname","distance","mass","radius"]
df=pd.DataFrame(list(zip (starsname,distance,mass,radius)),columns=headers)
df.to_csv('starsto.csv')