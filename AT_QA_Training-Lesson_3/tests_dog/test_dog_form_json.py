import requests


def test_get_check_content_type_json():
    response = requests.get("https://dog.ceo/api/breed/hound/list")
    assert response.headers["Content-Type"] == "application/json"
