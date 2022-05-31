import sys,re,json,math
from scipy import spatial
import pandas as pd
from datetime import date, timedelta
import requests
import os
from tqdm import tqdm
import time

relHashtags = ["#stopasianhate"]

hashs = pd.read_csv("Hashtags.csv")
relHashtags = list(hashs['Hashtag'])
relHashtags = list(set([x.lower() for x in relHashtags]))

print(relHashtags)

Api_Token = "PhlAcz7kVbFCmXbXMuYZFsfSbNi38uYzLSFHrspB"

DaysInterval = 355
currentDate = date.today()
numIntervals = 3
FilePath = "Posts/"
params = {
    "token" : Api_Token
}

for hastag in tqdm(relHashtags):
    tempDate = currentDate
    currPath = FilePath + "{}".format(hastag[1:])
    try:
        os.mkdir(currPath)
    except:
        continue
    for i in range(numIntervals):
        params["endDate"] = str(tempDate)
        params["searchTerm"] = hastag
        params["sortBy"] = "date"
        params["startDate"] = str(tempDate - timedelta(days=DaysInterval))
        tempDate = tempDate - timedelta(days=DaysInterval)
        params["count"] = 0
        while True:
            try:
                posts = requests.get("https://api.crowdtangle.com/posts/search", params=params)
                break
            except:
                continue
        try:
            count = posts.json()['result']['hitCount']
            numPages = int((count+99)/100)
            time.sleep(10)
            for i in range(numPages):
                params["count"] = 100
                params["offset"] = i*100
                while True:
                    try:
                        posts = requests.get("https://api.crowdtangle.com/posts/search", params=params)
                        break
                    except:
                        continue
                with open(currPath+"/File_{}_{}_{}.json".format(str(tempDate), str(tempDate - timedelta(days=DaysInterval)), i), "w") as f:
                    json.dump(posts.json(), f)
                time.sleep(10)
        except Exception as e:
            time.sleep(10)
            print("Error encountered - {}".format(e))
            continue