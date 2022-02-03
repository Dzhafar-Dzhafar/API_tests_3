import requests


def test_get_check_status_code_PR_equals_200():
    response = requests.get("https://jsonplaceholder.typicode.com/")
    assert response.status_code == 200
