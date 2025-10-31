import requests
import os
from dotenv import load_dotenv
import pandas as pd


def loadCards():
    load_dotenv()
    key = os.getenv("MY_API_KEY")
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {key}"
    }
    r = requests.get("https://api.clashroyale.com/v1/cards", headers=headers)
    data = r.json()
    cardsDF = pd.json_normalize(data["items"])
    towerTroopsDf = pd.json_normalize(data["supportItems"])
    cardsDF = cardsDF.set_index("name")
    pd.set_option('display.max_columns', None)
    print(cardsDF)



if __name__ == "__main__":
    loadCards()

