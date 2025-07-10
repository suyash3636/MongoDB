from pymongo import MongoClient
from pprint import pprint
from bson import ObjectId

con_url="mongodb+srv://suyash3636:ug7eAdLCDAKukD9Z@cluster0.zkh4sxj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(con_url)   

db=client.sample_analytics
col_accounts=db.accounts

# new_record={"accoun_id":895635,"limit": 10000,"product":["CurrencyService","Brokerage"]}

# result= col_accounts.insert_one(new_record)
# print(f"Inserted record with ID: {result.inserted_id}")



# res=col_accounts.find_one( {"_id" : ObjectId("685d044f826270591124ba54") })
# print("Found record:",res)


res=col_accounts.update_one({"_id": ObjectId ("5ca4bbc7a2dd94ee5816238c")},{ "$set" :{"limit" :11000}})
client.close()  