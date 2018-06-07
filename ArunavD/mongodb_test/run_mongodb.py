# import pymongo
from pymongo import MongoClient
client = MongoClient()
# Python module to use md5 (This code was used for MD5 hash of the password string)
import hashlib
# Access the database (change hridaydutta123 to your database name)
db = client['Arunav']
# Access the collections
details = db.details
myDetails = {
    'name':'Arunav Das',
    'email': 'arunavdas15@gmail.com',
    'github': 'ArunavD',
    'password': str(hashlib.md5('abcd1234'))
}
# Insert data into database
result = details.insert_one(myDetails)