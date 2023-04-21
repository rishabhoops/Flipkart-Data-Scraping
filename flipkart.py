import requests
import pandas as pd
from bs4 import BeautifulSoup
Product_Name=[]
Prices=[]
Descriptions=[]
Reviews=[]
for i in range(5):
    url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    r = requests.get(url)

    soup=BeautifulSoup(r.text,"html.parser")
    box=soup.find("div",class_="_1YokD2 _3Mn1Gg")
    names=box.find_all("div",class_="_4rR01T")
    prices=box.find_all("div",class_="_30jeq3 _1_WHN1")
    for i in names:
        name=i.text
        Product_Name.append(name)
    
        
    # print(Product_Name)

    for i in prices:
        name=i.text
        Prices.append(name)
        
    

    desc=box.find_all("ul",class_="_1xgFaf")

    for i in desc:
        name=i.text
        Descriptions.append(name)
        
    

    review=box.find_all("div",class_="_3LWZlK")
    for i in review:
        name=i.text
        Reviews.append(name)  
        
df=pd.DataFrame({"Product":Product_Name,"Price":Prices,"Descriptions":Descriptions,"Reviews":Reviews})
df.to_csv("flipkart dat.csv")