# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
# run with: uvicorn main:app --reload --host 0.0.0.0 --port 8000


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

LOCAL_PATH = os.path.dirname(__file__)
PODS_FILE = os.path.join(LOCAL_PATH, 'pod_records.json')


def insert_on_mongo_db(data):
	print('saving on the database')
	client = pymongo.MongoClient("mongodb+srv://engrogerio:micromint@cluster0-8khjs.mongodb.net/pygps?retryWrites=true&w=majority")
	db = client['pygps']
	pod = db['pods']
	id = pod.insert_one(data).inserted_id
	return id

def read_json(json_file: str):
	with open(json_file, 'r') as data:
		data ={[data]}
		print(data)
		#return json.load(data)

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
	id = insert_on_mongo_db(dict(pod))
	return f'{license_plate} - {id}'
	
app = FastAPI()
cademp=''


@app.post("/pod/")
async def add_record(pod: Pod):
	print('-->>', (pod))
	print(save_pod(pod))
	
	return pod
	
@app.get("/pod/")
async def list_pods():
	return get_pods()

@app.get("/pod/{licence_plate}", response_model=Pod, response_model_exclude_unset=True)
async def get_pods_by_license_plate(licence_plate: str):
	return Pod[licence_plate]
