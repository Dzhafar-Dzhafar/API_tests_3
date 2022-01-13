import pprint
import requests
import pytest

'''
r = requests.get('https://dog.ceo/api/breed/hound/list')

print("\n@status\nheaders\nencoding:")
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print("\n#text:")
print(r.text)
print("\n#json:")
print(pprint.pprint(r.json()))
print("\n#headers:")
for key, value in r.headers.items():
    print(key, ' => ', value)
'''


@pytest.fixture
def json_param():
    if "plott" in r:
        print('В списке пород есть plott')


r = requests.get('https://dog.ceo/api/breed/hound/list')

print("\n#json:")
print(pprint.pprint(r.json()))


def test_json_dog_1(json_param):
    return r.json()
