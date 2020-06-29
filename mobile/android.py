# this script works on qpython3 for android
# import needed modules
import androidhelper as android
import time
import sys, select, os #for loop exit
import requests
import datetime

LICENSE_PLATE = "EET2050"
# api
url = 'http://192.168.0.8:8000/pod'

#Initiate android-module
droid = android.Android()

#notify me
droid.makeToast("fetching GPS data")

print("start gps-sensor...")
droid.startLocating()

#txt = open ('/Download/coords.txt', 'a')
while True:
   
    location = droid.getLastKnownLocation().result
   
    lat = location['gps']['latitude']
    lgt = location['gps']['longitude']
    alt = location['gps']['altitude']
    tim = location['gps']['time']
    # geo = droid.geocode(lat, lgt, 1)
    # print(geo)
    # print(f'{lat} - {lgt} - {alt} - {tim}')
    json = dict()
    json["license_plate"] = LICENSE_PLATE
    json["latitude"] = lat
    json["longitude"] = lgt
    json["altitude"] = alt
    json["timestamp"] = str(datetime.datetime.now())
    print (json)
    requests.post(url, json = json)
    #txt.write(f'{lat} - {lgt} - {alt} - {tim} \n')
    time.sleep(5) #wait for 5 seconds

print("stop gps-sensor...")
droid.stopLocating()
