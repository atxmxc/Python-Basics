import requests
url = "https://dog.ceo/api/breeds/image/random"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Random Dog Image URL")
        print(data['message'])
    else:
        print("Failed", response.status_code)
except requests.exceptions.RequestException as e:
    print("Error", e)
