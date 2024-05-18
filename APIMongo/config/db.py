from pymongo import MongoClient

conn = MongoClient()
db = conn.local
collection_user = db.user
