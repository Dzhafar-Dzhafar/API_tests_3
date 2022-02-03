import requests


def test_get_response_json_contents_id_8_user_content():
    response = requests.get("https://jsonplaceholder.typicode.com/users/8")
    response_body = response.json()
    assert response_body['id'] == 8
    assert response_body["username"] == 'Maxime_Nienow'
    assert response_body['phone'] == "586.493.6943 x140"
    assert response_body["company"]['name'] == "Abernathy Group"
