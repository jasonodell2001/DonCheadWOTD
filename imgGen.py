import requests
import random
import pandas as pd
import wordListChecker as wlc

def genImg ():
    api_url = "https://api.imgflip.com/caption_image"
    wordList = pd.read_csv('wordList.csv').to_numpy()
    rng = random.randint(0, wordList.shape[0] - 1)
    while wordList[rng][1] != "N":
        rng = random.randint(0, wordList.shape[0] - 1)

    memeInfo = {"template_id": 343471833, "username": "", "password": "",
                "text0": "Don Cheadle " + wordList[rng][2] + " of the Day", "text1": wordList[rng][0], "max_font_size":40}

    response = requests.post(api_url, data=memeInfo)
    print(response.json())
    output = response.json()
    print(output['data']['url'])
    url = output['data']['url']

    v = pd.read_csv('wordList.csv')
    v.at[rng, 'Used'] = "Y"
    v.to_csv("wordList.csv", index=False)

    wlc.remainingWords() #check and print the number of unused words remaining
    return url
