import requests


def test_get_fragment_length_check_json_returned():
    response = requests.get("https://dog.ceo/api/breed/hound/list")
    response_body = response.json()
    assert len(response_body["message"]) == 7
