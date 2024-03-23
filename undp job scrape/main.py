import requests
import pandas as pd

from bs4 import BeautifulSoup

data = {'Job-Title': [],'Agency':[] ,'Post-Level': [], 'Location': [], 'Deadline': [],'Category': [], 'Job-Link': [] }




url ="https://jobs.undp.org/cj_view_jobs.cfm"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

links = soup.find_all("a", class_="vacanciesTableLink")

for link in links:
    href = link.get("href")
    if "cj_view_job.cfm?cur_job_id=" in href:
        cont = "https://jobs.undp.org/" + href
    
    #print(href)
    data["Job-Link"].append(href)    


a_elements = soup.find_all('a', class_='vacanciesTableLink')


for a_element in a_elements:
    
    title = a_element.find_all('span')[0]  
    if title:
       #print(title.get_text())
       data["Job-Title"].append(title.get_text())


for a_element in a_elements:
    
    category = a_element.find_all('span')[1]  
    if category:
       #print(category.get_text())  
       data["Category"].append(category.get_text())      



for a_element in a_elements:
    
    postLevel = a_element.find_all('span')[2]  
    if postLevel:
       #print(postLevel.get_text())    
       data["Post-Level"].append(postLevel.get_text())



for a_element in a_elements:
    
    date = a_element.find_all('span')[3]  
    if date:
       #print(date.get_text())    
       data["Deadline"].append(date.get_text())

for a_element in a_elements:
    
    agency = a_element.find_all('span')[5]  
    if agency:
       #print(agency.get_text()) 
        data["Agency"].append(agency.get_text())   


for a_element in a_elements:
    
    location = a_element.find_all('span')[6]  
    if location:
       #print(location.get_text())       
        data["Location"].append(location.get_text())    


df = pd.DataFrame.from_dict(data)   
df.to_csv("data.csv", index=False) 