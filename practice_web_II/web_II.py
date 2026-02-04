import webbrowser
import requests
import os
from bs4 import BeautifulSoup


url = "https://www.tzometcounseling.com/"

response = requests.get(url)

if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    print("Not Found.")

soup = BeautifulSoup(response.content, 'html.parser')
title = soup.title.string

print(title)

img_logo = soup.find("img")
print(img_logo)
img_url = img_logo.get("src")
print(img_url)
download_img_url = requests.get(img_url)
print(download_img_url)

with open("logo.png", "wb") as file:
    file.write(download_img_url.content)
webbrowser.open("https://static.wixstatic.com/media/c1e3b5_faa0d859c64c4e3e913a770d5b365dff~mv2.png/v1/fill/w_82,h_82,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/Tzomet%25252520logo%25252520july%252525202_edi.png")



headers = response.headers

for key, value in headers.items():
    print(f"{key} -> {value}")
