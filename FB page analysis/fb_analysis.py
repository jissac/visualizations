## Using Graph API: https://developers.facebook.com/tools/explorer/?method=GET&path=steam%3Ffields%3Dposts%7Bcomments.limit(0).summary(true)%2Ccreated_time%2Cmessage%2Clikes.limit(0).summary(true)%7D&version=v2.9
## Based on tutorial: http://www.kdnuggets.com/2017/06/6-interesting-things-facebook-python.html

import requests
import time
import pickle
import random
token = 'EAACEdEose0cBAFThpNu5P9LOezQCaq9Il9qc3UvNWT3nTatQjGwwSIob5jwVb37YyheiT3YJdNQKwhg7n74ZAsPvBGTrZBq6tXM0NqG2orX4pfpA6GffzhnV4fwbs84LOw0k4YDCTLQHbk1kr0mhHIAmFyAmRID8zJhEZCgRRz2Ui196PQDMaauZC2BxC2wZD'
req = '67919847338/posts?fields=comments,likes&limit=4'
# req = steam?fields=posts{comments.limit(0).summary(true),created_time,message,likes.limit(0).summary(true)}
def req_facebook(req):
    r = requests.get('https://graph.facebook.com/' + req, {'access_token' : token})
    return r

r = req_facebook(req)
results = r.json()

data = []


i = 0
while True:
    
    try:
        time.sleep(random.randint(2,5))
        data.extend(results['data'])
        r = requests.get(results['paging']['next'])
        results = r.json()
        i += 1
        
        if i > 5:
            break
    # paging throws an error if no more posts and ends loop
    except: 
        print 'done'
        break
        
pickle.dump(data, open('steam_data.pkl', 'wb'))
loaded_data = pickle.load(file=open('steam_data.pkl'))