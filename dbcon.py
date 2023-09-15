from flask import Flask, jsonify, request
from pymongo import MongoClient

client = MongoClient()
client = MongoClient("mongodb://localhost:27017/")
mydb = client.lodhaproject
table = mydb['users']

newval = {
    "OwnerName": "Caleb",
    "RegisteredName": "Caleb",
    "Email": "c@gmail.com",
    "Mobile": "7778889990",
    "FlatNo": "101",
    "ParkingSlot": "A/101",
    "Block": "A2",
    "Password": "Cal@1234",
    "Role": "admin",
    "Dues": 5000
}

x = table.insert_one(newval)

query = {"SELECT * from users"}

x = table.find()
for i in x:
    print(i)
