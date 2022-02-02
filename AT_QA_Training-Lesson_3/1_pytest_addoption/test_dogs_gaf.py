import pytest
import requests
import jsonschema

'''
@pytest.fixture()
def default_url():
    return "https://dog.ceo/api"


@pytest.fixture()
def pic_url():
    return "breeds/image/random"
'''

testdata = [1, 10, 20, 30, 40, 50]

"""
Проверка кода ответа и схемы json
"""


def test_res_200(default_url):
    response = requests.get(f"{default_url}/breeds/list/all",
                            verify=True)
    assert response.status_code == 200  # Проверяем статус код
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "object"},
            "status": {"type": "string"},
        },
        "required": ["message", "status"]
    }
    jsonschema.validate(instance=response.json(),
                        schema=schema)  # Способ проверки схемы json через validate "jsonchema"


""" Проверка количества фото собак в json с тем, что указано в url"""


@pytest.mark.parametrize("url_num", testdata)
def test_list_of_dogs(url_num, default_url, pic_url):
    response = requests.get(f"{default_url}/{pic_url}/{url_num}",
                            verify=True)  # f-строка для формирования url
    assert len(response.json().get(
        "message")) == url_num
    # Сравниваем количество файлов в json, в "message" с указанным в url, на 51 падает, так как лимит 50
