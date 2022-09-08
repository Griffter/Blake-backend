from typing import Union
from fastapi import FastAPI
import sys
import requests
import sqlite3
import json
from pydantic import BaseModel

app = FastAPI()

class User (BaseModel):
    name: str
    lastName: str
    insertion: str
    organisation:  str
    function: str
    assignedRole: str
    portalRol : str
    email:str
    phoneNumber :str
    
class Company (BaseModel):
    name: str
    adress: str
    sector: str
    price:  float
    is_offer: Unicon[bool, None] = None

class UserCompany (BaseModel):
    name: str
    price:  float
    is_offer: Unicon[bool, None] = None
    
    
class portalRol (BaseModel):
    managePersonalData : str
    manageNetworkData : str
        

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/company")
def read_root():
    return {"Show": "Companies"}

@app.get("/persons")
def read_root():
    return {"Show": "persons"}

@app.get("/person/{Pers_EmailAddress}")
def read_root():
    
    #The different request strings
    response = requests.get(mUrl, auth=('rimar', 'luaqp3glHFuco0R1Wrb9'), timeout=5, verify=False)
    data = response.json()
    json_str = json.dumps(data)  
    resp = json.loads(json_str)

for searchMail in resp['$resources']:
     personId = searchMail['Pers_PersonId']
     persFirstName = searchMail['Pers_FirstName']
     persLastName = searchMail['Pers_LastName']
     persNctvAansrpeek = searchMail['pers_nctv_aanspreek']
     persCompanyId = searchMail['Pers_CompanyId']
     persNctv_aanspreking = searchMail['pers_nctv_aanspreking']
     persNctv_taranisid = searchMail['pers_nctv_taranisid']

     print("------Persoon gegevens SageCRM-----------")   
     print("Personeels ID")
     print(personId)
     print("-----------------")
     print("Voornaam:" + persFirstName)
     print("-----------------")
     print("Achternaam:" + persLastName)
     print("-----------------")
     print("Aanspreekpunt:")
     print(persNctvAansrpeek)
     print("-----------------")
     print("Personeels company Id:")
     print(persCompanyId)
     print("-----------------")
     print("Ncsc Taranis id persoon:")
     print(persNctv_taranisid)
     print("-----------------")
     print("Ncsc aanspreking persoon:")
     print(persNctv_aanspreking)
     print("-----------------")
     print("Ncsc Taranis id persoon:")
     print(persNctv_taranisid)
     print("-----------------")
     print("-----------------")


@app.get("/company/{Comp_CompanyId}")
def read_companyid():
    
    #Get comapny based on user company id
    cResponse = requests.get(cUrl, auth=('rimar', 'luaqp3glHFuco0R1Wrb9'), timeout=5, verify=False)
    cData = cResponse.json()
    comp_json_str = json.dumps(cData)
    cResp = json.loads(comp_json_str)

for comp in cResp['$resources']:
     compName = comp['Comp_Name']
     compTitle = comp['$title']
     compType = comp['Comp_Type']
     CompStatus = comp['Comp_Status']
     CompIntegratedSystems = comp['Comp_IntegratedSystems']
     compNctvMegatronid = comp['comp_nctv_megatronid']
     compNctvTaranisid = comp['comp_nctv_taranisid']
     compMemberShipId = comp["comp_membershipid"]
      
     print("------ bijhorende Company Persoon gegevens SageCRM-----------")          
     print("-----------------")
     print("-----------------")   
     print("Company Name:")
     print(compName)
     print("-----------------")
     print("Tilte:" + compTitle)
     print("-----------------")
     print("Company type:" + str(compType))
     print("-----------------")
     print("Company status :")
     print(CompStatus)
     print("-----------------")
     print("Personeels company Id:")  
     print(persCompanyId)
     print("-----------------")
     print("Company Integrated Systems:")
     print(CompIntegratedSystems)
     print("-----------------")    
     print("company Nctv Megatronid:")
     print(compNctvMegatronid)
     print("-----------------")
     print("company Nctv Taranisid")
     print(compNctvTaranisid)
     print("-----------------")
     print("Company membership id")
     print(compMemberShipId)
     print("-----------------")
     print("-----------------")
     print("--------In memory Dictonary key value---------")
    #return {"Show": "Company ID"}


iamrole_dict = {"person_id": personId,
     
                     "person_firstname": persFirstName,
                     "person_insertion": "",
                     "person_lastname": persLastName,
                     "person_company_id": persCompanyId,
                     "person_ncsc_aanspreek": persNctvAansrpeek,
                     "person_ncsc_taranis_id": persNctv_taranisid,
                     "company_id ": persCompanyId,
                     "company_title": compTitle,
                     "company_type": compType,
                     "company_integrated_systems": CompIntegratedSystems,
                     "company_ncsc_megatron": compNctvMegatronid,
                     "company_ncsc_taranis_id": compNctvTaranisid,
                     "company_Membership_id": compMemberShipId,
                     "person_roles": "",}
print(iamrole_dict)


@app.get("/persons/{comp_id}")
def read_compid_person(comp_id: int):
    
    for pers in resp['$resources']:
         if persCompanyId == comp['comp_id']:
                personId = searchMail['Pers_PersonId']
                persFirstName = searchMail['Pers_FirstName']
                persLastName = searchMail['Pers_LastName']
                persNctvAansrpeek = searchMail['pers_nctv_aanspreek']
                persCompanyId = searchMail['Pers_CompanyId']
                persNctv_aanspreking = searchMail['pers_nctv_aanspreking']
                persNctv_taranisid = searchMail['pers_nctv_taranisid']
    
    return {"All person with company ID": comp_id}


# @app.get("/person/{email}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
