# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI() 
cademp=''

with open('c:/users/rsilva/source/fastapi/data.json') as file:
    cademp = json.load(file)

class Cademp(BaseModel):
    cd_number: str
    status: str	
    common_name: str
    legal_name: str
    street: str
    postal_code: str
    city: str
    province: str
    province_name: str
    country: str
    country_name: str
    cnpj: str
    ie: str
    business_phone: str
    email: str
    is_carrier: str


@app.post("/cademp", response_model=Cademp)
async def create_supplier(cademp: Cademp):
    return cademp

@app.get("/cademp")
async def list_supplier():
    return cademp

@app.get("/cademp?cdnumber={cd_number}", response_model=Cademp, response_model_exclude_unset=True)
async def read_supplier(cd_number: str):
    return cademp[cd_number]

@app.get("/cademp/{cd_number}/cnpj", response_model=Cademp, response_model_include={"common_name", "cnpj"},)
async def read_supplier_name(cd_number: str):
    return cademp[cd_number]