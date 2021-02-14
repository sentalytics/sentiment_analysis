from helpers import exceptions
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://root:<PASSWORD>@cluster0.mmscg.mongodb.net/sentiment?retryWrites=true&w=majority")
db = cluster["sentiment"]
collection = db["comments"]

def insert(item):
    try:
        return collection.insert_one(item)
    except Exception as e:
        exceptions.handle_error('Failed insert into "comments"', e)

def find(query):
    try:
        return collection.find(query)
    except Exception as e:
        exceptions.handle_error('Failed find in "comments"', e)

def batch_insert(items):
    try:
        return collection.insert_many(items)
    except Exception as e:
        exceptions.handle_error('Failed batch insert into "comments"', e)

# Danger
def drop_collection(colName):
    if colName == "comments":
        try:
            return collection.drop()
        except Exception as e:
            exceptions.handle_error('Failed to drop "comments"', e)
