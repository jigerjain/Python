import requests

# Url
url = 'http://ec2-18-234-69-105.compute-1.amazonaws.com/issues/login.php'

# Payload username and password for your application
payload = {'username':'testuser','password':'test'}
r = requests.post(url,data=payload)

print(r.status_code)

# To check if there is any string like "Incorrect" or "Invalid" 
# Since status code for both valid and invalid requests is same 200
if 'incorrect' in r.text:
	print('Incorrect')
#print(r.text)
