import requests
import pandas as pd

from bs4 import BeautifulSoup

data = {'Job-Title': [], 'Description': [], 'Agency': ["UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF","UNICEF",],  'Location': [], 'Deadline': [], 'Job-Link': []}




url ="https://jobs.unicef.org/en-us/listing/"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

Tit = soup.select("a.job-link")

for a in Tit:
     print(a.string)
     data["Job-Title"].append(a.string)
     



for link in Tit:
       full_link = "https://jobs.unicef.org" + link.get("href")
       print(full_link)
       data["Job-Link"].append(full_link)
       




#for child in soup.find_all(class_="row--teaser").children:
#    print(child)

des = soup.find_all("div",class_="row--teaser")


for row_teaser_div in des:
   
    p_tags = row_teaser_div.find_all("p")
    
    #print(len(p_tags))
    print(p_tags[1].get_text(),"n/")
    data["Description"].append(p_tags[1].get_text())




loc = soup.select("span.location")

for location in loc:
    print(location.string)
    data["Location"].append(location.string)

deadLine = soup.select("span.close-date")

for date in deadLine:
    print(date.string)
    data["Deadline"].append(date.string)
    

df = pd.DataFrame.from_dict(data)   
df.to_csv("data.csv", index=False) 