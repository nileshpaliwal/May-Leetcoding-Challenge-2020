
import pyrebase

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
#cred = credentials.Certificate(r'C:\Users\Nilesh\Desktop\FoGraphProject\FoGraphWeb\fographcommunity-firebase-adminsdk-b4drk-5f2cf1d287.json')
cred = credentials.Certificate(r'C:\Users\Nilesh\Desktop\FoGraphProject\FoGraphWeb\fographcommunity-firebase-adminsdk-b4drk-5f2cf1d287.json')
firebase_admin.initialize_app(cred)

db = firestore.client()



config = {
    'apiKey': "AIzaSyCYeyUGfQHb_VZsKbs5B-rmIwBF-M6UjOo",
    'authDomain': "fographcommunity.firebaseapp.com",
    'databaseURL': "https://fographcommunity.firebaseio.com",
    'projectId': "fographcommunity",
    'storageBucket': "fographcommunity.appspot.com",
    'messagingSenderId': "700249724896",
    'appId': "1:700249724896:web:f140eeda9ffd8a92a33d85",
    'measurementId': "G-HF68EBLMYC"
} 

firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database = firebase.database()
a = "zia29a8XwxXIa36NNFC5myZ06LJ3"




url = "https://us-central1-fographcommunity.cloudfunctions.net/generateUserFeed?uid=zia29a8XwxXIa36NNFC5myZ06LJ3&startAfterComm=FoGraph_Portrait&startAfterPost=1589442742"


url = "https://us-central1-fographcommunity.cloudfunctions.net/generateUserFeed?uid=zia29a8XwxXIa36NNFC5myZ06LJ3"

import requests
r = requests.get(url)
r = r.content


t = []
import json

test = json.loads(r.decode('utf-8')) 

for i in test:
    t.append(i)



for i in test:
    print(i)
    print("------------")










    
    
    



