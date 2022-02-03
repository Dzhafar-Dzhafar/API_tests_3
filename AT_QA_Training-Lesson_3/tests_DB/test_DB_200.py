import requests


def test_get_check_status_code_equals_200():
    response = requests.get("https://www.openbrewerydb.org/")
    assert response.status_code == 200
