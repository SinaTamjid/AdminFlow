import pymongo as mg
from flask import Flask
#connection data
client=mg.MongoClient("mongodb://localhost:27017/")
db_user=client["Users"]
collection_user=db_user["user_info"]

def InsertDoc(collection_name,Username,password,email,valid=False):


               collection_name.insert_one({
                              "Username":str(Username),
                              "password":str(password),
                              "email":str(email),
                              "valid":bool(valid)
               })
               



def ShowDoc(collection_name):

               cursor=collection_name.find()
               for x in cursor:
                print(x)
               

def UpdateDoc(collection_name,Username,key,value):

               collection_name.update_one({"Username":str(Username)

               },{"$set":{str(key):str(value)}})

InsertDoc(collection_user,"sara","sarapassword","sara@gmail.com")
UpdateDoc(collection_user,"sara","Username","sara_dst")

show=ShowDoc(collection_user)
print(show)