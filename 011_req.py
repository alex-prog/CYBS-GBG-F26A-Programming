# we need to install the requests library first using pip install requests
# pip install requests
# or
# pip3 install requests
# or
# python -m pip install requests
# import requests

# response = requests.get("https://ek.dk")
# print(response.status_code) # Prints 200 if things go well
# # print(response.text) 

# ---------------------------------------
# import requests

# payload = {'username': 'alice', 'password': 'strongpassword'}
# response = requests.post("https://httpbin.org/post", data=payload)
# print(response.text)

# ---------------------------------------
# import requests
# from requests.auth import HTTPBasicAuth
# response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('Alice', 'strongpassword'))
# print(response.status_code)


# ---------------------------------------
import requests
session = requests.Session()

session.get('https://httpbin.org/cookies')

response = session.get('https://httpbin.org/cookies')
print(response.text)
