import pymongo
import os
from decouple import config


client = pymongo.MongoClient(
    config('HOST')
)
mydb = client[config('DATABASE')]
collection = mydb["members"]