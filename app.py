from flask import Flask
from mongoengine import connect
from api import *
from pymongo import MongoClient


app= Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db':'Library',
    'host':'localhost',
    'port': 27017
}

connect(**app.config['MONGODB_SETTINGS'])

pymongo_client = MongoClient("mongodb://localhost:27017/")
pymongo_db = pymongo_client["Library"]

app.register_blueprint(api)

if __name__== '__main__':
    app.run()

