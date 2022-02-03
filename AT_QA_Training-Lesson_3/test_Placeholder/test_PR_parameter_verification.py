import requests


def test_get_check_bs_id_7():
    response = requests.get("https://jsonplaceholder.typicode.com/users/7")
    response_body = response.json()
    assert response_body["company"]["bs"] == "generate enterprise e-tailers"
