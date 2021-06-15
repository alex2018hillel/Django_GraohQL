import requests





response1 = requests.post(
    'http://127.0.0.1:8000/graphql/',
    json = {'mutation': { 'createActor' : {input: { 'name': "1234" } }}},
    # headers={'Content-Type': 'application/json'},
)

response = requests.post(
    'http://127.0.0.1:8000/graphql/',
    json = {'query': '{ actors { name } }'},
    headers={'Content-Type': 'application/json'},
)

json_response = response.json()
print(json_response)
repository = json_response['data']['actors']
for i in repository:
    print(i)
# print(f'Repository name: {repository["name"]}')  # Python 3.6+
# print(f'Repository description: {repository["description"]}')
#

