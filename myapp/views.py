import django
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from datetime import date
from firebase_admin import initialize_app, db, credentials
import time as t
import pywifi
import json, csv

config = {
    'apiKey': "AIzaSyA1BMgLRSWkHjIQZKtAGzzQz5vGh64nDCQ",
    'authDomain': "wifiscanner-a0843.firebaseapp.com",
    'databaseURL': "https://wifiscanner-a0843-default-rtdb.firebaseio.com",
    'projectId': "wifiscanner-a0843",
    'storageBucket': "wifiscanner-a0843.appspot.com",
    'messagingSenderId': "123196091842",
    'appId': "1:123196091842:web:2f435bb9bafac1deceba5b",
    'measurementId': "G-R4D99KH07K"
}
cred = credentials.Certificate('wifiscanner-a0843-firebase-adminsdk-zqiyb-c8d7ee0f31.json')
firebase_app = initialize_app(cred, config)

def get_current_time():
    current_date_time = datetime.now()
    current_date = current_date_time.date()
    current_time = current_date_time.time()
    return current_date, current_time

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def post_data(storage_url, jsonfile):
    data = read_json_file(jsonfile)
    ref = db.reference(storage_url)
    ref.push().set(data)
    
def home(request):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    results = []
    iface.scan()
    t.sleep(0.2)
    current_date, current_time = get_current_time()
    
    scan_results = iface.scan_results()
    storage_url = "NetworkList"
    
    for data in scan_results:
        if data.ssid == "":
            continue
        result = {
            'date': current_date.isoformat(),
            'time': current_time.isoformat(),
            'ssid': data.ssid,
            'rssi': data.signal,
            'freq': data.freq,
            'bssid': data.bssid
        }
        results.append(result)
        with open('results.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(result.values())
    
    with open('new_information.json', 'w') as jsonfile:
        json.dump(results, jsonfile, indent=4)
        
    data = read_json_file("new_information.json")
    post_data(storage_url, 'new_information.json')
    
    context = {
        'results': results
    }

    return render(request, 'scan.html', context)
def index(request):
    return render(request, 'index.html')
def list(request):
    return render(request, 'show.html')