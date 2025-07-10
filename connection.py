from pymongo import MongoClient
from pprint import pprint
from bson import ObjectId  # ← Import this for ObjectId

con_url = "mongodb+srv://suyash3636:ug7eAdLCDAKukD9Z@cluster0.zkh4sxj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(con_url)
db = client["restaurant"]

db_names = client.list_database_names()
for db_name in db_names:
    print(f"\n➡️  Database: {db_name}")
    db = client[db_name]
    

    # List all collections in the current DB
    collections = db.list_collection_names()
    if not collections:
        print("  (No collections)")
    else:
        for col_name in collections:
            print(f"  🗂️  Collection: {col_name}")
            collection = db[col_name]

            # Print 3 sample documents
            print("    📄 Sample documents:")
            for doc in collection.find().limit(3):
                pprint(doc)