import requests
from bs4 import BeautifulSoup
import csv

url1 = "https://www.aajenterprises.com/ecommerce-companies-in-india/"
url2 = "https://www.clickpost.ai/blog/ecommerce-companies-in-india"


def scrape_aaj():
    resp=requests.get(url1)
    resp.raise_for_status()
    soup=BeautifulSoup(resp.text, "html.parser")
    results=[]
    sections=soup.find_all("h3")
    for sec in sections:
        title=sec.get_text(strip=True)
        results.append(title)
    return results


def scrape_clickpost():
    resp=requests.get(url2)
    resp.raise_for_status()
    soup=BeautifulSoup(resp.text, "html.parser")
    results=[]
    table=soup.find("div", class_="blog__post--table__format--section--inner")
    if not table:
        return results
    tbody=table.find("tbody")
    if not tbody:
        return results
    rows=tbody.find_all("tr")
    for row in rows:
        a_tag=row.find("a")
        if a_tag:
            results.append(a_tag.get_text(strip=True))
    return results

def savCsv(filename,data_list):
    with open(filename,"w",newline="",encoding="utf-8") as f:
        writer=csv.writer(f)
        for item in data_list:
            writer.writerow([item])


def main():
    print("\nAAJ Enterprises:")
    a=scrape_aaj()
    for x in a:
        print("-", x)
    savCsv("AAJ.csv",a)

    print("\n\n\nClickPost:")
    c=scrape_clickpost()
    for x in c:
        print("-", x)
    savCsv("Clickpost.csv",c)

main()
