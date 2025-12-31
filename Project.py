import requests
from bs4 import BeautifulSoup

url=input("Enter website:")
print("\n\n\n\n")

response=requests.get(url)
response.raise_for_status()

soup=BeautifulSoup(response.text,"html.parser")

elements=soup.find_all("div",class_="page")
for page in elements:
    title = page.find("h3", class_="page-title").get_text(strip=True)
    link = page.find("a")
    desc = page.find("p", class_="lead session-desc").get_text(strip=True)
    print(title,":\n")
    print("\t",desc)
    print("\nLink:",link)
    #https://www.scrapethissite.com/pages/