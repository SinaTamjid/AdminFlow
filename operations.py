

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

               collection_name.update_one({"Username":str(Username)},
                                          {"$set":{str(key):str(value)}})

def Verified(collection_name,email):
               collection_name.update_one({"email":str(email)},{"$set":{"valid":bool(True)}})

