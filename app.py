from flask import Flask, request
from flask_cors import CORS
import controller



import json
import os
import socket
import subprocess
import sys
import threading
import time
from threading import Timer


# Variables app Flask
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}}) # Acepta dede todas las direcciones con el *


machine_ip = '192.168.130.79'
json_data = ''


@app.route('/',methods=['GET'])
def get():
    return 'ASTRO Server'


@app.route('/',methods=['POST'])
def executor():
    global json_data
    data_recived = request.json
    json_data = data_recived

    print('Solicitud')
    if 'action' in json_data:

        if json_data['action'] == 'add_user':
            pass
        if json_data['action'] == 'get_user':
            print('GET USERS')
            algo = controller.get_user()
            return algo

if __name__ == '__main__':
    app.run(debug= True, host= machine_ip)
    # app.run(debug= True)