import requests


def test_get_check_equals_user_13():
    response = requests.get("https://jsonplaceholder.typicode.com/users/13")
    response_body = response.json()
    assert response_body == {}
