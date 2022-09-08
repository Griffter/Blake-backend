from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

userRequestMail = ""
url = "mock-data/vCompany.json"

class Company (BaseModel):
    Id: int
    name: str
    adress: str
    sector: str
    title:str
    type: str
    status:str

class User (BaseModel):
    id: int
    name: str
    lastName: str
    insertion: str
    organisation:  str
    function: str
    assignedRole: str
    portalRol : str
    email:str
    phoneNumber :str
    
class UsersCompany (BaseModel):
    userCompanyID : int
    name: str
    lastname: str
    companyID: int
    price:  float
    
class portalRol (BaseModel):
    managePersonalData : str
    manageNetworkData : str
        

@app.get("/companies/{comp_id}")
def read_root():
    return {getCompanies}

@app.get("/companies/{comp_id}/persons")
def read_root():
     return {getCompanies}

@app.get("/person/{Pers_EmailAddress}")
def read_root():
    return {"Show": "persons with email adress"}

@app.post("/person/{Pers_EmailAddress}")
def read_root():
    return {"Show": "persons with email adress"}

@app.post("/company/{comp_id}/persons")
def read_root():
    return {"Update company info"}


@classmethod
def getCompanies(compid):
    
    cData = url.json()
    comp_json_str = json.dumps(cData)
    cResp = json.loads(comp_json_str)
    
    for comp in cResp['$resources']:
        if compid == comp['Comp_CompanyId']:
            Company.name = comp['Comp_Name']
            Company.title = comp['$title']
            Company.type = comp['Comp_Type']
            Company.status = comp['Comp_Status']
            
    comp_dict = {
                     "company_id ": compid,
                     "company_title": Company.title,
                     "company_type": Company.type,
                     "company_name": Company.name,
    }
    
    print("testing" + comp_dict) 
    print(cResp)