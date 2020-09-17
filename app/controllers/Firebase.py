import pyrebase

def getStorage():
    firebaseConfig = {
        "apiKey": "AIzaSyD-jmiO9xNi7wQqAcpcJbg4twG2leJlcVk",
        "authDomain": "kjsd-410e7.firebaseapp.com",
        "databaseURL": "https://kjsd-410e7.firebaseio.com",
        "projectId": "kjsd-410e7",
        "storageBucket": "kjsd-410e7.appspot.com",
        "messagingSenderId": "552677017355",
        "appId": "1:552677017355:web:2b8416a07b5d197d5a440e"
    }

    firebase = pyrebase.initialize_app(firebaseConfig)

    storage = firebase.storage()
    
    return storage
