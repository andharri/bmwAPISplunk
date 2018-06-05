import requests
import json

varBMWVIN = "myVIN"
varBMWUser = "user@domain.com"
varBMWPassword = "s3cr5t"
varSplunkURL = "https://mysplunkurl.com:8088/services/collector"
varSplunkKey = "splunk-key"

# Get BMW API Token
url = "https://customer.bmwgroup.com/gcdm/oauth/authenticate"

header = {
	'Host':	'customer.bmwgroup.com',
	'Origin': 'https://customer.bmwgroup.com',
	'Accept-Encoding': 'br, gzip, deflate',
	'Content-Type': 'application/x-www-form-urlencoded',
	'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 Mobile/15B150 Safari/604.1',
	'Origin': 'https://customer.bmwgroup.com'
}

form = {
	'client_id': 'dbf0a542-ebd1-4ff0-a9a7-55172fbfce35',
	'response_type': 'token',
	'username': varBMWUser,
	'password': varBMWPassword,
	'redirect_uri':	'https://www.bmw-connecteddrive.com/app/default/static/external-dispatch.html',
	'scope': 'authenticate_user fupo',
	'state': 'eyJtYXJrZXQiOiJnYiIsImxhbmd1YWdlIjoiZW4iLCJkZXN0aW5hdGlvbiI6ImxhbmRpbmdQYWdlIiwicGFyYW1ldGVycyI6Int9In0',
	'locale': 'GB-en'
}

r = requests.post(url, params=header, data=form, allow_redirects=False)

# Make API call
token = r.headers['location'].split("&")[1].split("=")[1]
url = "https://www.bmw-connecteddrive.co.uk/api/vehicle/dynamic/v1/"+varBMWVIN
headers = {"Authorization":"Bearer "+token}
r = requests.get(url, headers=headers, allow_redirects=False)

# Dump JSON response into Splunk HEC
authHeader = {'Authorization': 'Splunk '+varSplunkKey}
jsonDict = {"event": json.loads(r.text)}
r = requests.post(varSplunkURL, headers=authHeader, json=jsonDict, verify=False)
