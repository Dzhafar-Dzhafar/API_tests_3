import requests


def test_get_check_encoding_equals_utf8():
    response = requests.get("https://www.openbrewerydb.org/projects")
    assert response.encoding == "UTF-8"
