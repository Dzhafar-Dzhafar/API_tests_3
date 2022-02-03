import requests


def test_get_check_word_in_fragment_json_returned(word_search='blood'):
    response = requests.get("https://dog.ceo/api/breed/hound/list")
    response_body = response.json()
    assert word_search in (response_body["message"])
