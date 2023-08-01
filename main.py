import redis

import requests
from fastapi import FastAPI

rd = redis.Redis(host="localhost", port=6379, db=0)
app = FastAPI()

@app.get("/")
def read_root():
    return "Hello World"

@app.get("/fish/{species}")
def read_fish(species:str):
    cache = rd.get(species)
    if cache:
        print("cache hit")
        print(cache)
        return 1
    else:
        print("cache miss")
        r = requests.get(f"https://www.fishwatch.gov/api/species/{species}")
        rd.set(species, r.text)
        print(r)
        return 2
