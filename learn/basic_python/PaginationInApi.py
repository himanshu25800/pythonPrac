import requests
import json


def getResponse(url : str , pageNumber , pageSize, totalPages) -> dict:

    limit = pageSize
    offset = (pageNumber-1)*pageSize
    # print(offset)

    if offset > totalPages :
        return {}

    response = requests.get(url+f"?limit={limit}&offset={offset}")

    if response.status_code == 200:
        return response.json()


def getPages(data):
    return data["work_count"]

url = "https://openlibrary.org/subjects/science.json?limit=10&offset=0"
pageNumber = 1
pageSize = 1000

data = getResponse(url , pageNumber , pageSize , 0)
totalPages = getPages(data)

count = 0
while(True):
    count += 1
    data = getResponse(url , pageNumber , pageSize , totalPages)
    # print(data)
    pageNumber +=1
    if len(data)==0:
        break
    print(count)

    
print(count)


# data = getResponse(url)
# print(data)
# print(data['total'])