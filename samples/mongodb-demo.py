# pymongo == 4.0.1
from pymongo import MongoClient

client = MongoClient(host="127.0.0.1", port=27017, username="admin", password="123456")

dblist = client.list_database_names()

print(dblist)