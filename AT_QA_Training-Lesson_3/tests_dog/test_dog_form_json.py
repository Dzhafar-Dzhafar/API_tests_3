import requests


def test_get_locations_for_us_90210_check_content_type_equals_json():
    response = requests.get("https://dog.ceo/api/breed/hound/list")
    assert response.headers["Content-Type"] == "application/json"