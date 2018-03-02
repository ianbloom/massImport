#!/bin/env python

import requests
import json
import hashlib
import base64
import time
import hmac
import os

#Account Info

AccessId = input("Enter LM Access ID: ")
AccessKey = input("Enter LM Access Key: ")
Company = input("Enter Account Site Trimmed: ")
#AccessId ='dSpe6j9eTQXs3Iph7jCU'
#AccessKey ='dcm!p2d2w79V=5f}+[354xL=g{k442Y6h5qV}C_6'
#Company = 'ianbloom'

#Initialize fileArray variable to hold filepath for all dataSources
os.chdir(os.path.dirname(__file__))
currentWorkingDirectory = os.getcwd()
fileArray = []
hmacArray = []

#Iterate through files in CWD, if file ends in .xml then assume it is a datasource and add it to fileArray
for filename in os.listdir(currentWorkingDirectory):
	if filename.endswith(".xml"):
		fileArray.append(os.path.join(currentWorkingDirectory,filename))
	else:
		continue

for i in range(len(fileArray)):
	#File Information
	fileName = fileArray[i]
	file = open(fileName,'r')
	xml = file.read()

	#Request Info
	httpVerb ='POST'
	resourcePath = '/setting/datasources/importxml'
	queryParams =''
	data = '''------WebKitFormBoundary12345BUlKhOAAA1X
Content-Disposition: form-data; name="file"; filename="''' + fileName + '''"
Content-Type: text/xml

''' + xml + '''

------WebKitFormBoundary12345BUlKhOAAA1X--'''

	#Construct URL 
	url = 'https://' + Company + '.logicmonitor.com/santaba/rest' + resourcePath + queryParams

	#Get current time in milliseconds
	epoch = str(int(time.time() * 1000))

	#Concatenate Request details
	requestVars = httpVerb + epoch + data + resourcePath

	hmacArray.append(hmac.new(AccessKey.encode(),msg=requestVars.encode(),digestmod=hashlib.sha256).hexdigest())
	signature = base64.b64encode(hmacArray[i].encode())

	#Construct headers
	auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
	headers = {'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundary12345BUlKhOAAA1X','Authorization':auth}

	#Make request
	#print('url= ', url)
	#print('data=', data)
	#print('headers= ', headers)

	response = requests.post(url, data=data, headers=headers)

	#Print status and body of response
	print('Response Status:',response.status_code)
	print('Response Body:',response.content)