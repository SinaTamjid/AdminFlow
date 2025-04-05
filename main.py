import pymongo as mg

from flask import Flask,Request,render_template
from operations import *
#connection data
client=mg.MongoClient("mongodb://localhost:27017/")
db_user=client["Users"]
collection_user=db_user["user_info"]
#flask app
app=Flask(__name__)

@app.route("/",methods=['POST','GET'])
def Home():
   return render_template("index.html")



if '__main__'==__name__:
               app.run(debug=True)

# InsertDoc(collection_user,"sara","sarapassword","sara@gmail.com")
# UpdateDoc(collection_user,"sara","Username","sara_dst")

# show=ShowDoc(collection_user)
# print(show)