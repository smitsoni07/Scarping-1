from bs4 import BeautifulSoup
import os
import pandas as pd

d = {
    'Title':[],
    'Price':[],
    'Link':[]
}

for file in os.listdir('data1'):
    try:
        with open(f"data1/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        t = soup.find("h2")
        title = t.get_text()
        
        l = t.find("a")
        link = "https://amazon.in/" + l['href']
        
        p = soup.find("span", attrs={"class":"a-price-whole"})
        price = p.get_text()
        
        d['Title'].append(title)
        d['Price'].append(price)
        d['Link'].append(link)
        
    except Exception as e:
        print(e)
        
df = pd.DataFrame(data=d)
df.to_csv("data1.csv")