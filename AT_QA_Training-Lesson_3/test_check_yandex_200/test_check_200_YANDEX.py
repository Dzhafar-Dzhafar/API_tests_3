import requests


def test_get_check_yandex_status_code_200():
    response_yandex = requests.get("https://ya.ru")
    assert response_yandex.status_code == 200
