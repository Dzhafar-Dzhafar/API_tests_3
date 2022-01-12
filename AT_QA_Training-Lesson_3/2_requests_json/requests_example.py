import pprint
import requests

r = requests.get('https://jsonplaceholder.typicode.com/posts/1')

print("\n------- status/headers/encoding ---------")
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print("\n----------------- text ------------------")
print(r.text)
print("\n----------------- json ------------------")
print(pprint.pprint(r.json()))
print("\n---------------- headers ----------------")
for key, value in r.headers.items():
    print(key, ' => ', value)

