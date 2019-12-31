import bs4
from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as soup
import json
def get_json_data(user_id):
    my_url = "https://osu.ppy.sh/api/get_user?k=d00c8066f200234347434baf854fe3a5e25509f6&u=**&m=0&type=id"
 
    my_url = my_url.replace("**",str(user_id))
 
    req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
    uClient = 0
    i = 1
    while (uClient == 0): # Keep trying to make request
        try:
            uClient = uReq(req)
        except Exception:
            print("critical failure in the url request:", my_url)
            if i == 3: # if too many failed attempts...
                print("skipping request")
                return None # just end it
            i += 1
            uClient = 0
            time.sleep(60*10) # wait 10 minutes. 
            
    page_html = uClient.read()
    page_html = page_html.decode('utf-8')
    uClient.close()
 
    page_soup = soup(page_html,"html.parser")
 
    player_text = page_soup.text
 
    if player_text == "[]":
        print("Invalid Entry")
        return None
 
    try:
        player_dicts = json.loads(player_text)
    except Exception as error:
        print(error)
        return None
 
    output = []
    for player_dict in player_dicts:
        #player_label = list(player_dict.keys())
        player_list = list(player_dict.values())
        output.append(player_list)
    
    #assert(len(player_list == player_label))
    # in this case we have nested lists. We are only requesting the first element
    # of the output list, which has "user data". 
    return output[0][:-1] # in this case, we a have nested lists. 
 
#=============



#get_json_data(4787150)
#output.append(player_list)
 
 
## Next phase ===========================
label = ['user_id', 'username', 'join_date', 'count300', 'count100', 'count50',
         'playcount', 'ranked_score', 'total_score', 'pp_rank', 'level',
         'pp_raw', 'accuracy', 'count_rank_ss', 'count_rank_ssh',
         'count_rank_s', 'count_rank_sh', 'count_rank_a', 'country',
         'total_seconds_played', 'pp_country_rank']
print("label length:", len(label))

import csv
import time

f = open('user.csv', 'a')
g = open('user2.csv', 'a')
h = open('user3.csv', 'a')
 
w = csv.writer(f)
w.writerow(label)
w = csv.writer(g)
w.writerow(label)
w = csv.writer(h)
w.writerow(label)
 
w = csv.writer(f)

broken_users = []

with open('player_ids.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    count = 1 # starting increment
    i = 1
    for row in csvReader:
        if i % 2 == 0:
            i += 1
            continue
        i += 1
        #print("row id", row[0])

        try:
            data = get_json_data(row[0])
        except Exception as error:
            print("Error",error)
            broken_users.append(row[0])
            count += 1 # counting this user
            continue # go on with the next user

        # we are expecting a list of 21 elements
        if data is None:
            broken_users.append(row[0])
            count += 1 # also counting this user
            continue # continue with the next user.

        w.writerow(data)
        count += 1
        
        # printing progress... there are 87328 users to go through.
        if count % 100 == 0:
            print(count/87328, "%")
        elif count % 10 == 0:
            print(".")

        # deciding if we should change files (so we don't have 1 super large csv file)
        if count > 29109 and count <= 58218:
            if not f.closed:
                w = csv.writer(g)
                f.close() # close the first csv file
        if count > 58218:
            if not g.closed:
                w = csv.writer(h)
                g.close()

        time.sleep(1.15) # wait so we don't overload the server api.
        # the limit is 60 requests per minute. 
        
h.close()
print("Here are broken users", broken_users)
print("congrats...")
