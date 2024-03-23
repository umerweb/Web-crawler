import requests

def fetchAndSaveToFile(url,path):
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)

url = "https://jobs.unicef.org/en-us/listing/"        

fetchAndSaveToFile(url,"data2/jobs.html")