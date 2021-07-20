import requests

response1 = requests.post(
    'http://127.0.0.1:8000/graphql/',
    json = {'query': '{ actors { name } }'},
    headers={'Content-Type': 'application/json'},
).json()['data']['actors']

response2 = requests.post(
    'http://127.0.0.1:8000/graphql/',
    json = {'query': '{ movies { id, title } movie (id: 2) { id, title } }'},
    headers={'Content-Type': 'application/json'},
)

response3 = requests.post(
    'http://127.0.0.1:8000/graphql/',
    json = {'query': '{ movie (id: 2) { id, title } }'},
    headers={'Content-Type': 'application/json'},
)

# print(response1)
# for i in response1:
#     print(i["name"])
#
# json_response2 = response2.json()
# print(json_response2)
# repository = json_response2['data']['movies']
# for i in repository:
#     print(i)
#
# json_response3 = response3.json()
# print(json_response3)
# repository = json_response3['data']['movie']
# print(repository['title'])




# response222 = requests.post(
#     'http://127.0.0.1:8000/graphql/',
#     # json = {'mutation': '{ createActor(input: { name: Toms Hanks } ) {ok, actor {id,name}} }'},
#     json = {'mutation': "{ createActor(input: { 'name': 'Toms Hanks' } ) {'ok', actor{'id','name'}} }"},
#     headers={'Content-Type': 'application/json'},
# )
# print(response222)

url = 'http://127.0.0.1:8000/graphql/'
headers={'Content-Type': 'application/json'}
variables = { 'actor' :{'id', 'name'}}

query = """
mutation createActor {
  createActor(input: {
    name: "Tom1 Hanks"
  }) {
    ok
    actor {
      id
      name
    }
  }
}
"""

def make_query(query, url, headers):
    """
    Make query response
    """
    request = requests.post(url, json={'query': query}, headers=headers) #, 'variables': variables
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

a = make_query(query, url, headers)# variables,
print(a)

