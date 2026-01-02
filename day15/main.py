# http, get vs post and status codes
# API'S are basically asking a url for data and its respons with JSON
# 2 methods, GET vs POST (GET Today ONLY)

import requests
'GET /weather?city=london'  # example of using GET
'POST /login'  # example of using POST
# GET recieves data while POST sends data

# Status Codes
'200 = OK'
'400 = BAD REQUEST'
'401 = UNAUTHORIZED'
'403 = FORBIDDEN'
'404 = NOT FOUND'
'429 = TOO MANY REQUESTS'
'500 = SERVER ERROR'
# now we can use a new library, requests
# here is a little example
# response = requests.get("https://api.github.com")
# data = response.json()
# print(type(data))
# print(data)
# print(response.status_code)
# print(response.text)
# this is a safe way of requesting data
url = "https://api.github.com"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Request Failed:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Network Error:", e)
