import bs4

from urllib.request import urlopen as uReq
from urllib.request import Request

from bs4 import BeautifulSoup as soup

import time # so we don't overload on the page scraping

chars = ["US","RU","DE", "PL", "FR", "JP","CA", "BR", "GB", "TW", "KR","CN","AU","ID","UA", "PH", "CL", "FI", "AR", "NL", "SE", "SG", "MX", "ES","MY", "IT", "HK", "TH", "VN", "NO"]
my_url = "https://osu.ppy.sh/rankings/osu/performance?country=@@&page=**#scores"

def get_req(req):
    return uReq(req)

def country_parse(temp_url):
    output = []
    # 201
    for i in range(1,201):
        time.sleep(1)
        my_url = temp_url.replace("**",str(i))
        req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
        uClient = 0
        while (uClient == 0):   
            try:
                uClient = uReq(req) # opens a connection, and dowload. (it's a client)
            except:
                print("critical failure in the request:", my_url)
                time.sleep(60*30) # wait 20 minutes
        #dumping contents
        page_html = uClient.read() #The web_byte is a byte object returned by the server and the content type present in webpage is mostly utf-8.
        page_html = page_html.decode('utf-8')
        uClient.close()

        page_soup = soup(page_html,"html.parser")

        containers = page_soup.findAll("tr",{"class":"ranking-page-table__row"})

        min_cap = 2900
        
        for container in containers:
            #we are only expecting a list of size 1
            td_container = container.findAll("td",
                                             {"class" : "ranking-page-table__column ranking-page-table__column--focused"})

            #extract the performance
            player_performance = td_container[0].text.strip()

            if int(player_performance.replace(",","")) <= min_cap:
                return output

            a_container = container.findAll("a",{"class" : "ranking-page-table__user-link-text js-usercard"})

            str_a_container = str(a_container)

            start = str_a_container.find("https://osu.ppy.sh/users/")

            end = str_a_container.find('">')

            player_user_id = str_a_container[start+25:end]

            output.append(int(player_user_id))

    return output


import csv


lable = ["user_id"]

f = open('player_ids.csv','a')
w = csv.writer(f)
counter = 1
for e in chars:
    data = country_parse(my_url.replace("@@",e))

    for row in data:
        print(counter)
        w.writerow([row])
        counter += 1

f.close()
