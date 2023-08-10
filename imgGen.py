import requests
import random
import pandas as pd
def genImg ():
    api_url = "https://api.imgflip.com/caption_image"
    username = ""
    password = ""
    memeID = "343471833"
    wordList = pd.read_csv('wordList.csv').to_numpy()
    rng = random.randint(0, wordList.shape[0] - 1)
    while wordList[rng][1] != "N":
        rng = random.randint(0, wordList.shape[0] - 1)

    memeInfo = {"template_id": 343471833, "username": "", "password": "",
                "text0": "Don Cheadle Word of the Day", "text1": wordList[rng][0]}

    response = requests.post(api_url, data=memeInfo)
    print(response.json())
    output = response.json()
    print(output['data']['url'])
    url = output['data']['url']
    v = pd.read_csv('wordList.csv')
    v.at[rng, 'Used'] = "Y"
    v.to_csv("wordList.csv", index=False)
    return url
