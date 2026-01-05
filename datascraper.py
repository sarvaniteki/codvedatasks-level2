import requests
from bs4 import BeautifulSoup
import csv
res=requests.get("https://www.cbse.gov.in")
print("the status code is",res.status_code)
print("\n")
soup_data= BeautifulSoup(res.text,"html.parser")
print(soup_data.title)
print("\n")
headlines=soup_data.find_all('h4')
cbsc_titles = []
for headline in headlines:
    title = headline.get_text(strip=True)
    if title:
        news_titles.append(title)
with open("CBSC_headlines.csv","w",newline="",encoding="utf-8")as file:
    writer = csv.writer(file)
    writer.writerow(["Headline"])
    for title in cbsc_titles:
        writer.writerow([title])
print(f"{len(cbsc_titles)} headlines saved to cbsc_headlines.csv")
