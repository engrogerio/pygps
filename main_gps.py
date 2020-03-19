# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

from typing import List
import pymongo
from fastapi import FastAPI
from pydantic import BaseModel
import json
import os



class Pod(BaseModel):
    license_plate: str = None
    latitude: float = None
    longitude: float = None
    altitude: float = None
    timestamp: str = None

PODS_FILE = 'c:/users/rsilva/source/fastapi/pod_records.json'


def db_insert_on_mongo_db(data):
    client = pymongo.MongoClient("mongodb+srv://engrogerio:micromint@cluster0-8khjs.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test_database
    collection = db.test_collection
    posts = db.posts
    post_id = posts.insert_one(data).inserted_id
    return post_id

def read_json(json_file: str):
    with open(json_file, 'r') as data:
        return json.load(data)

def write_json(pod: Pod, json_file: str):
    with open(json_file, 'a') as data:
        data.write(str(dict(pod)).replace("'", '"'))
        data.write('\n')
    return pod.license_plate

def get_pods():
    pods = read_json(PODS_FILE)
    return pods

def save_pod(pod: Pod):
    license_plate = write_json(pod, PODS_FILE)
    return license_plate
    
app = FastAPI()
cademp=''


@app.post("/pod/")
async def add_record(pod: Pod):
    print('-->>', (pod))
    save_pod(pod)
    return pod
    
@app.get("/pod/")
async def list_pods():
    return get_pods()

@app.get("/pod/{licence_plate}", response_model=Pod, response_model_exclude_unset=True)
async def get_pods_by_license_plate(licence_plate: str):
    return Pod[licence_plate]