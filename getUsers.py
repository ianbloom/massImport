#!/bin/env python

import requests
import json
import hashlib
import base64
import time
import hmac

#Account Info

#AccessId = input("Enter LM Access ID: ")
#AccessKey = input("Enter LM Access Key: ")
#Company = input("Enter Account Site Trimmed: ")
AccessId ='dSpe6j9eTQXs3Iph7jCU'
AccessKey ='dcm!p2d2w79V=5f}+[354xL=g{k442Y6h5qV}C_6'
Company = 'ianbloom'

#File Information
fileName = '/Users/ianbloom/Documents/massImport/Noisiest_DataSources.xml'
#fileName = 'Noisiest_DataSources.xml'
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

hmac = hmac.new(AccessKey.encode(),msg=requestVars.encode(),digestmod=hashlib.sha256).hexdigest()
signature = base64.b64encode(hmac.encode())

#Construct headers
auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
headers = {'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundary12345BUlKhOAAA1X','Authorization':auth}

#Make request
response = requests.post(url, data=data, headers=headers)

#Print status and body of response
print('Response Status:',response.status_code)
print('Response Body:',response.content)