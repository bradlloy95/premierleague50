import requests
import json


token = 'c1536bfd2888413b84d5341baa1dc770'
id = 57
#endpoint = 'https://api.football-data.org/v4/competitions/PL/teams'
endpoint = f"https://api.football-data.org/v4/teams/{id}"


headers = {'X-Auth-Token': token}

response = requests.get(endpoint, headers=headers)
data = response.json()
print(data)