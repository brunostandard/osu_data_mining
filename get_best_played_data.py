import bs4
from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as soup
import json
def get_json_data(user_id):
    my_url = "https://osu.ppy.sh/api/get_user_best?k=d00c8066f200234347434baf854fe3a5e25509f6&u=**&m=0&type=id"
 
    my_url = my_url.replace("**",str(user_id))
 
    req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
    uClient = 0
    i = 1
    while (uClient == 0): # Keep trying to make request
        try:
            uClient = uReq(req)
        except:
            print("critical failure in the url request:", my_url)
            if i == 3:
                # too much time wasted
                print("skipping request")
                return None
            i += 1
            uClient = 0
            time.sleep(60*10)
            
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
    #print(player_label)
    #print(player_list)
    #assert(len(player_list == player_label))
    return output
 
 
## Testing phase =====================
 
#user_id = 914004
#test = get_json_data(user_id)
#for row in test:
#    print(row)
lable = ['beatmap_id', 'score_id', 'score', 'maxcombo', 'count50', 
'count100', 'count300', 'countmiss', 'countkatu', 'countgeki', 'perfect', 
'enabled_mods', 'user_id', 'date', 'rank', 'pp']
 
#output.append(player_list)
 
 
## Next phase ===========================
 
##import csv
##import time
## 
##f = open('best_played.csv', 'a')
##g = open('best_played2.csv', 'a')
##h = open('best_played3.csv', 'a')
## 
##w = csv.writer(f)
##w.writerow(lable)
##w = csv.writer(g)
##w.writerow(lable)
##w = csv.writer(h)
##w.writerow(lable)
## 
##w = csv.writer(f)
##
##
##with open('player_ids.csv') as csvDataFile:
##    csvReader = csv.reader(csvDataFile)
##    count = 1 # starting increment
##    i = 1
##    for row in csvReader:
##        if i % 2 == 0: # every even'th row is a blank b/c csv issues
##            i += 1
##            continue
##        i += 1
##        
##        try:
##            data = get_json_data(row[0])
##        except Exception as error:
##            print("Error",error)
##            count += 1 # counting the skip
##            continue # with next user
##        
##        # we are expecting 10 rows of information
##        if data is None:
##            continue # with the loop of user_ids
##        
##        for row_data in data: # we have a nested list
##            w.writerow(row_data)
##        print(count) # one success story to the command line.
##        
##        count += 1
##
##        # The last part is just dealing with the csv files. Poorly written...
##        if count > 29109 and count <= 58218: # start writing in the second csv file
##            w = csv.writer(g)
##            f.close() # close the first csv file
##        if count > 58218: # start writing on the thrid csv file
##            w = csv.writer(h)
##            g.close() # close the second csv file
##            
##        time.sleep(1.15) # wait so we don't overload the server api
## 
##h.close() # close the third/last csv file.
##
##print("congrats...")
