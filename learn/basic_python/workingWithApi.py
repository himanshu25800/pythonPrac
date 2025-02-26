import requests
import json

url = "https://reqres.in/api/users?page=2"

response = requests.get(url)

if(response.status_code == 200):
    print(response)
    data = response.json()
    # print(data)

    # saving json data to the file
    with open("response.json","w") as file:
        json.dump(data , file)

    for row in data["data"]:
        print(row["avatar"])
