import requests

endpoint = "http://localhost:1010/pdrf"

get_response = requests.get(endpoint, json={"query": "Hello World"})
print(get_response.text)
print(get_response.status_code)

print(get_response.json()['messages'])
# print(get_response.status_code)