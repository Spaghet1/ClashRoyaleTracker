import requests
import json
import os
from dotenv import load_dotenv, dotenv_values
import pandas as pd

if __name__ == "__main__":
    load_dotenv()
    myKey = os.getenv("MY_API_KEY")
    print(myKey)


#r=requests.get("https://api.clashroyale.com/v1/players/%23UQ2RGGVLR", headers={"Accept":"application/json", "authorization":"Bearer " + myKey}, params = {"limit":20})

#print(r.text)
#print(json.dumps(r.json(), indent = 2))
#df = pd.DataFrame(r.json()["data"])
#print(df)