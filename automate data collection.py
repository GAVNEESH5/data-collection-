import requests
from bs4 import BeautifulSoup

url ="https://www.ndtv.com/"
response = requests.get(url)
html_content= response.text

soup = BeautifulSoup(html_content, "html.parser")

headlines =soup.find_all(['h2','h3'])

headlines_text = []

for headline in headlines:
    text = headline.get_text(strip=True)
    if text:
        headlines_text.append(text)

with open("headlines.text","w", encoding="utf-8") as file:
    for headline in headlines_text:
        file.write(headline+"\n")
print("headlines saves to headlines.text")