
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

# Use ChromeDriverManager to automatically download and install the appropriate ChromeDriver
#webdriver_path = ChromeDriverManager().install()
#browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

webdriver_path = ChromeDriverManager().install()

# Create the WebDriver instance
browser = webdriver.Chrome(options=options)

print('\n\n\n', "------------- PROFILE FETCHER v1 -------------\n")

jobTitle = input("[*] Enter Job Title: ")
location = input("[*] Enter Location: ")

url = f"http://www.google.com/search?q=+%22{jobTitle}%22+%22{location}%22 -intitle:%22profiles%22 -inurl:%22dir/%22 +site:in.linkedin.com/in/ OR site:in.linkedin.com/pub/&num=100"

# add'+%22Cybersecurity%22' to the above link to check whether the logic of checking if a company is a cybersecurity company or not working. 

#"CEO" "Delhi" -intitle:"profiles" -inurl:"dir/"  site:in.linkedin.com/in/ OR site:in.linkedin.com/pub/

# First level: div class="MjjYud"
# Second level: div class="g Ww4FFb vt6azd tF2Cxc asEBEc"
# Third level: div class="kvH3mc BToiNc UK95Uc"
# Fourth level: div class="Z26q7c UK95Uc jGGQ5e"
# Fifth level: div class="yuRUbf"
# Sixth level: anchor tag <a>

browser.get(url)
soup = BeautifulSoup(browser.page_source, 'html.parser')
divs = soup.find_all('div', {'class': 'MjjYud'})
print("Count: " + str(len(divs)))

links = []
bios = []
cyberchecks = []
names = []

for div in divs:
    try:
        second_div = div.find('div', {'class': 'g Ww4FFb vt6azd tF2Cxc asEBEc'})
        third_div = second_div.find('div', {'class': 'kvH3mc BToiNc UK95Uc'})
        fourth_div = third_div.find('div', {'class': 'Z26q7c UK95Uc jGGQ5e'})
        fifth_div = fourth_div.find('div', {'class': 'yuRUbf'})
        link = fifth_div.find('a')['href']
        links.append(link)
    except Exception as e:
        print(f"An error occurred while processing: {str(e)}")

for newdiv in divs:
    try:
        newsecond_div = newdiv.find('div', {'class': 'g Ww4FFb vt6azd tF2Cxc asEBEc'})
        newthird_div = newsecond_div.find('div', {'class': 'kvH3mc BToiNc UK95Uc'})
        newfourth_div = newthird_div.find('div', {'class': 'Z26q7c UK95Uc'})
        newfifth_div = newfourth_div.find('div', {'class': 'VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf'})
        newbio = newfifth_div.find('span')
        bios.append(newbio.text)
    except Exception as e:
        print(f"An error occurred while processing: {str(e)}")

'''

for cybercheck in divs:  
	try:
			new_second_div = cybercheck.find('div', {'class': 'g Ww4FFb vt6azd tF2Cxc asEBEc'})
			new_third_div = new_second_div.find('div', {'class': 'kvH3mc BToiNc UK95Uc'})
			new_fourth_div = new_third_div.find('div', {'class': 'Z26q7c UK95Uc'})
			new_fifth_div = new_fourth_div.find('div', {'class': 'VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf'})
			newcybercheck = new_fifth_div.find('span')
			if 'cybersecurity' or 'security' or 'cyber security' in newcybercheck.lower():
				cyberchecks.append('Y')
			else:
				cyberchecks.append('N')
	except Exception as e:
		print(f"An error occurred while processing the div: {str(e)}")
                
for name in divs:
    try:
        _newsecond_div = name.find('div', {'class': 'g Ww4FFb vt6azd tF2Cxc asEBEc'})
        _newthird_div = _newsecond_div.find('div', {'class': 'kvH3mc BToiNc UK95Uc'})
        _newfourth_div = _newthird_div.find('div', {'class': 'Z26q7c UK95Uc jGGQ5e'})
        _newfifth_div = _newfourth_div.find('div', {'class': 'yuRUbf'})
        _newsixth_div = _newfifth_div.find('div', {'class': 'LC20lb MBeuO DKV0Md'})
        indexone = _newsixth_div.find('>')
        indexend = _newsixth_div.find('-') -1
        newname = _newsixth_div[indexone+1:indexend]
        names.append(newname)
    except Exception as e:
        print(f"An error occurred while processing: {str(e)}")
'''
        
keywords = ['cybersecurity', 'security', 'cyber security', "ciso", "cio", "cto"]
for newdiv in divs:
    try:
        newsecond_div = newdiv.find('div', {'class': 'g Ww4FFb vt6azd tF2Cxc asEBEc'})
        newthird_div = newsecond_div.find('div', {'class': 'kvH3mc BToiNc UK95Uc'})
        newfourth_div = newthird_div.find('div', {'class': 'Z26q7c UK95Uc'})
        newfifth_div = newfourth_div.find('div', {'class': 'VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf'})
        newcybercheck = newfifth_div.find('span')
        if any(keyword in newcybercheck.text.lower() for keyword in keywords):
            cyberchecks.append('Y')
        else:
            cyberchecks.append('N')
    except Exception as e:
        print(f"An error occurred while processing the div: {str(e)}")

for newdiv in divs:
    try:
        newsecond_div = newdiv.find('div', {'class': 'g Ww4FFb vt6azd tF2Cxc asEBEc'})
        newthird_div = newsecond_div.find('div', {'class': 'kvH3mc BToiNc UK95Uc'})
        newfourth_div = newthird_div.find('div', {'class': 'Z26q7c UK95Uc jGGQ5e'})
        newfifth_div = newfourth_div.find('div', {'class': 'yuRUbf'})
        newname = newfifth_div.find('a').text.split('-')[0].strip()
        names.append(newname)
    except Exception as e:
        print(f"An error occurred while processing: {str(e)}")


#old code that is not functional, will remove this after solving all errors. 		
'''
for cybercheck in divs:
    try:
        new_second_div = cybercheck.find('div', {'class': 'g Ww4FFb vt6azd tF2Cxc asEBEc'})
        new_third_div = new_second_div.find('div', {'class': 'kvH3mc BToiNc UK95Uc'})
        new_fourth_div = new_third_div.find('div', {'class': 'Z26q7c UK95Uc'})
        new_fifth_div = new_fourth_div.find('div', {'class': 'VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf'})
        newcybercheck = new_fifth_div.find('span')
        if find_CyberSecurity(newcybercheck) == False:
            cyberchecks.append('N')
        else:
            cyberchecks.append('Y')
        #cyberchecks.append(newcybercheck.text)
    except Exception as e:
        print(f"An error occurred while processing: {str(e)}")
        
'''

filename = f"profiles_{jobTitle}_{location}.csv"

with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Links", "names", "Bio", "CyberSecurity(Y/N)"])
    for link, bio, cybercheck in zip(links, names, bios, cyberchecks):
        writer.writerow([link, names, bio, cybercheck])

print(f"[+] Links saved to '{filename}' file.")
