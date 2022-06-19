from flask import Flask,request
import sqlite3
import json
import serial
app = Flask(__name__)

# You can also save the data directly into the database using the sqlite3 module and the commented codes.

@app.route('/')
def welcome():
    return 'Welcome to transport system api'


# def get_db_connection():
#     conn = sqlite3.connect('database.db')
#     conn.row_factory = sqlite3.Row
#     return conn


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        data = request.get_json()
        stringData = json.dumps(data)        

        if not stringData:
            print('data is required!')
        else:
            
            
            # conn = get_db_connection()
            # conn.execute('INSERT INTO transactions (amount, destination) VALUES (?, ?)',
            #              (amount, destination))
            # conn.commit()
            # conn.close()
            ser = serial.Serial(
                port='COM36',  # plz change this according to your port number
                baudrate=9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )


            
            
            ser.write(bytes(stringData), 'utf-8')
            ser.flush()
            print("Transaction stored succesfully")
    return 'Transaction sent  successfully'
            

    
