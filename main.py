import requests 
import json
from bs4 import BeautifulSoup 


def login():
    '''
    link = 'https://www.linkedin.com'
    p = 
    '''
    URL = 'https://www.linkedin.com'
    s = requests.Session()
    rv = s.get(URL + '/uas/login?trk=guest_homepage-basic_nav-header-signin')
    p = BeautifulSoup(rv.content, "html.parser")
    print(p)

login()
