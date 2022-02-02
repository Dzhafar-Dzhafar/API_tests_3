import requests


def test_get_content_response_sub_breed_dog_breed():
    response = requests.get("https://dog.ceo/api/breed/hound/list")
    response_body = response.json()
    assert response_body["message"] == ["afghan", "basset", "blood", "english", "ibizan", "plott", "walker"]
