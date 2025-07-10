from pymongo import MongoClient
from pprint import pprint
from bson import ObjectId  # ← Import this for ObjectId

con_url = "mongodb+srv://suyash3636:ug7eAdLCDAKukD9Z@cluster0.zkh4sxj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(con_url)
db=client["sample_training"]
collection_trip=db['trips']



result= collection_trip.aggregate( [{"$match":{'start station name':"Central Park S & 6 Ave"}},{'$group' :{"_id":'$usertype','count':{'$count':{}}}}])
for i in result:
    print(i)



# for db in client.list_database_names():
#     print(db)

# res=collection_trip.aggregate([{'$group':{'_id' :'$start station name','count': {'$count' :{}}}},{'$sort':{'count':-1}},{'$limit':15}])
# for i in res:
#     print(i)