import requests


def test_get_check_status_code_200():
    response = requests.get("https://dog.ceo/dog-api/documentation/sub-breed")
    assert response.status_code == 200