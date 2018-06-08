from pymongo import MongoClient
import hashlib
client=MongoClient()

#to access the database 

db=client["<dbname>"] #database connection

details=db.details #ACCESS THE COLLECTION

print(db) #CHECK IF DB IS CONNECTED
'''
	just like Dictionaries:
		d={"key":value}
		d["key"]=====> gives=('value')
'''

# you will only be able to append Dictionary inside Database

#
#m=hashlib.md5()

myDetails = {
	"Name" : "Name",
	"EmailID" : "email.com",
	"phNumber" : 12345678

}

#insert the data into the database
result = details.insert_one(myDetails)
