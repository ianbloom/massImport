#!/bin/env python

import requests
import json
import hashlib
import base64
import time
import hmac
import os
import json as _json

#Collect account info from user
AccessId = raw_input("Enter LM Access ID: ")
AccessKey = raw_input("Enter LM Access Key: ")
Company = raw_input("Enter Account Site Trimmed: ")

#################################
###                           ###
###   ROOT LEVEL PROPERTIES   ###
###                           ###
#################################

print('ROOT LEVEL PROPERTIES\n')

hmacArray = []

for i in range(3):
	#Request Info
	httpVerb ='POST'
	resourcePath = '/device/groups/1/properties'
	queryParams =''
	if i == 0:
		data = '{"name":"lmaccess.id","value":"' + AccessId + '"}'
	if i == 1:
		data = '{"name":"lmaccess.key","value":"' + AccessKey + '"}'
	if i == 2:
		data = '{"name":"lmaccount","value":"' + Company + '"}'

	#Construct URL 
	url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath +queryParams

	#Get current time in milliseconds
	epoch = str(int(time.time() * 1000))

	#Concatenate Request details
	requestVars = httpVerb + epoch + data + resourcePath

	#Construct signature
	hmacArray.append(hmac.new(AccessKey.encode(),msg=requestVars.encode(),digestmod=hashlib.sha256).hexdigest())
	signature = base64.b64encode(hmacArray[i].encode())

	#Construct headers
	auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
	headers = {'Content-Type':'application/json','Authorization':auth}

	#Make request
	response = requests.post(url, data=data, headers=headers)

	#Print status and body of response
	print("Payload:",data)
	print('Response Status:',response.status_code)
	print('Response Body:',response.content)
	print('\n')


########################
###                  ###
###   LOGICMODULES   ###
###                  ###
########################

#Change Working Directory to where this script is located
os.chdir(os.path.dirname(__file__))
currentWorkingDirectory = os.getcwd()
logicmoduleFolder = currentWorkingDirectory + "/DataSources (and LogicModules)"

#Initialize fileArray variable to hold filepath for all dataSources
fileArray = []
hmacArray = []

#######################
###                 ###
###   DATASOURCES   ###
###                 ###
#######################

print('DATASOURCES\n')

#Iterate through files in CWD/DataSources (and LogicModules), if file ends in .xml then assume it is a datasource and add it to fileArray

for filename in os.listdir(logicmoduleFolder):
	if filename.endswith(".xml"):
		fileArray.append(os.path.join(logicmoduleFolder,filename))
	else:
		continue

#Iterate through the dataSources and add each to LM
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

	#Construct signature
	hmacArray.append(hmac.new(AccessKey.encode(),msg=requestVars.encode(),digestmod=hashlib.sha256).hexdigest())
	signature = base64.b64encode(hmacArray[i].encode())

	#Construct headers
	auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
	headers = {'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundary12345BUlKhOAAA1X','Authorization':auth}

	#Make request
	response = requests.post(url, data=data, headers=headers)

	#Print status and body of response
	print('Filename:',fileArray[i])
	print('Response Status:',response.status_code)
	print('Response Body:',response.content)
	print('\n')

# Reset fileArray and hmacArray to be used again
fileArray = []
hmacArray = []

###########################
###                     ###
###   PROPERTYSOURCES   ###
###                     ###
###########################

print('PROPERTYSOURCES\n')

#Iterate through files in CWD/DataSources (and LogicModules), if file ends in .json then assume it is a propertysources and add it to fileArray
for filename in os.listdir(logicmoduleFolder):
	if filename.endswith(".json"):
		fileArray.append(os.path.join(logicmoduleFolder,filename))
	else:
		continue

#Iterate through the PropertySources and add each to LM
for i in range(len(fileArray)):
	#File Information
	fileName = fileArray[i]
	file = open(fileName,'r')
	json = file.read()

	#Request Info
	httpVerb ='POST'
	resourcePath = '/setting/propertyrules/import'
	queryParams =''
	data = '''--XXX
Content-Disposition: form-data; name="file"; filename="''' + fileName + '''"
Content-Type: multipart/form-data

''' + json + '''

--XXX--'''

	#Construct URL 
	url = 'https://' + Company + '.logicmonitor.com/santaba/rest' + resourcePath + queryParams

	#Get current time in milliseconds
	epoch = str(int(time.time() * 1000))

	#Concatenate Request details
	requestVars = httpVerb + epoch + data + resourcePath

	#Construct signature
	hmacArray.append(hmac.new(AccessKey.encode(),msg=requestVars.encode(),digestmod=hashlib.sha256).hexdigest())
	signature = base64.b64encode(hmacArray[i].encode())

	#Construct headers
	auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
	headers = {'Content-Type':'multipart/form-data; boundary=XXX','X-Version':'2','Authorization':auth}

	#Make request
	response = requests.post(url, data=data, headers=headers)

	#Print status and body of response
	print('Filename:',fileArray[i])
	print('Response Status:',response.status_code)
	print('Response Body:',response.content)
	print('\n')

##############################
###                        ###
###   DEAD DEVICES GROUP   ###
###                        ###
##############################

print('DEAD DEVICES GROUP\n')

# Build a dictionary to circumvent quotation mark escaping difficulties with AppliesTo statement
jsonDict = {}
jsonDict["name"] = "Dead Devices"
jsonDict["appliesTo"] = "auto.device_state =~ \"dead\""
data = _json.dumps(jsonDict, ensure_ascii=False)

httpVerb ='POST'
resourcePath = '/device/groups'
#Construct URL 
url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath

#Get current time in milliseconds
epoch = str(int(time.time() * 1000))

#Concatenate Request details
requestVars = httpVerb + epoch + data + resourcePath

#Construct signature
step1 = hmac.new(AccessKey.encode(),msg=requestVars.encode(),digestmod=hashlib.sha256).hexdigest()
signature = base64.b64encode(step1.encode())

#Construct headers
auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
headers = {'Content-Type':'application/json','Authorization':auth}

#Make request
response = requests.post(url, data=data, headers=headers)

#Print status and body of response
print('Response Status:',response.status_code)
print('Response Body:',response.content)

