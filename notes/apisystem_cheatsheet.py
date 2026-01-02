response = requests.get("https://api.github.com")

print(response.status_code)
'200 = OK (success)'
'400 = Bad request'
'401 = Unauthorized'
'403 = Forbidden'
'404 = Not found'
'429 = Too many requests'
'500 = Server error'
print(response.text)

data = response.json()
print(type(data))   # dict or list
print(data)
{
    "message": "https://dog.jpg",
    "status": "success"
}
print(data["message"])

requests.get(url, timeout=5)

except requests.exceptions.RequestException as e:
    print("Network error:", e)
