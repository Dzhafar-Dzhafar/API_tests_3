import requests


def test_get_response_json_elements_id_10():
    response = requests.get("https://jsonplaceholder.typicode.com/users/10")
    response_body = response.json()
    assert len(response_body) == 8
