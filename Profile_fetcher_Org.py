# Profile Fetcher
# Uses Google SERP to scrape LinkedIn profile links 
# Prone to IP blocking so use with a VPN if possible

import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time


options = ChromeOptions()
options.add_argument("--headless")
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5829.0 Safari/537.36')

webdriver_path = ChromeDriverManager().install()
browser = webdriver.Chrome(webdriver_path, options=options)
#browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

print('\n\n\n',"------------- PROFILE FETCHER v1 -------------\n")

jobTitle = input("[*] Enter Job Title: ")
location = input("[*] Enter Location: ")


url = f"http://www.google.com/search?q=+%22{jobTitle}%22+%22{location}%22 -intitle:%22profiles%22 -inurl:%22dir/%22 +site:in.linkedin.com/in/ OR site:in.linkedin.com/pub/&num=100"

# First level: div class="MjjYud"
# Second level: div class="g Ww4FFb vt6azd tF2Cxc asEBEc"
# Third level: div class="kvH3mc BToiNc UK95Uc"
# Fourth level: div class="Z26q7c UK95Uc jGGQ5e"
# Fifth level: div class="yuRUbf"
# Sixth level: anchor tag <a>

browser.get(url)
soup = BeautifulSoup(browser.page_source, 'html.parser')
divs = soup.find_all('div', {'class':'MjjYud'})
print("Count: " + str(len(divs)))

links = []

for div in divs:
    try:
        second_div = div.find('div', {'class':'g Ww4FFb vt6azd tF2Cxc asEBEc'})
        third_div = second_div.find('div', {'class':'kvH3mc BToiNc UK95Uc'})
        fourth_div = third_div.find('div', {'class':'Z26q7c UK95Uc jGGQ5e'})
        fifth_div = fourth_div.find('div', {'class':'yuRUbf'})
        link = fifth_div.find('a')['href']
        links.append(link)
    except:
        pass
    

filename = f"profiles_{jobTitle}_{location}.csv"
with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Links"])
    writer.writerows([[link] for link in links])

print(f"[+] Links saved to '{filename}' file.")