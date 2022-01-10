from pymongo import MongoClient
from flask import *  
from datetime import datetime, time
import socket
import json 
import csv

app = Flask(__name__)  
app.secret_key = "abc"  

mongoURL ='mongodb://localhost:27017/' or 'mongodb+srv://Vaishnavi:Vaishnavi@cluster0.jxaxu.mongodb.net/test?retryWrites=true&w=majority'
client = MongoClient(mongoURL)

db = client['Database']

information = db["data"]

@app.route('/login',methods = ['POST'])  
def login():  
      uname=request.form['uname']
      passwrd=request.form['password']
      postedAt = datetime.now()
      hostname = socket.gethostname()
      ipAdd = socket.gethostbyname(hostname)
      record = {
          'IPAddress': ipAdd,
          'data': {
              'uname': uname,
              'password': passwrd
          },
          'time': postedAt
      }
      information.insert_one(record)
      with open('json_file.json') as json_file:
        jsondata = json.load(json_file)
 
      data_file = open('data_file.csv', 'w', newline='')
      csv_writer = csv.writer(data_file)
 
      count = 0
      for data in jsondata:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
      csv_writer.writerow(data.values())
 
      data_file.close()
      return "Pushed"
   
if __name__ == '__main__':  
   app.run(debug = True)  