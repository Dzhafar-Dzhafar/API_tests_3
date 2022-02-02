import requests


def test_get_check_status_code_201_206():
    res_1 = requests.get("https://dog.ceo/dog-api/documentation/sub-breed")
    x_norm_1 = [201, 206]
    assert res_1.status_code <= x_norm_1[0] or res_1.status_code >= x_norm_1[1]


def test_get_check_status_code_100_103():
    res_2 = requests.get("https://dog.ceo/dog-api/documentation/sub-breed")
    x_norm_2 = [100, 103]
    assert res_2.status_code <= x_norm_2[0] or res_2.status_code >= x_norm_2[1]


def test_get_check_status_code_300_308():
    res_3 = requests.get("https://dog.ceo/dog-api/documentation/sub-breed")
    x_norm_3 = [300, 308]
    assert res_3.status_code <= x_norm_3[0] or res_3.status_code >= x_norm_3[1]


def test_get_check_status_code_400_417():
    res_4 = requests.get("https://dog.ceo/dog-api/documentation/sub-breed")
    x_norm_4 = [400, 417]
    assert res_4.status_code <= x_norm_4[0] or res_4.status_code >= x_norm_4[1]


def test_get_check_status_code_500_505():
    res_5 = requests.get("https://dog.ceo/dog-api/documentation/sub-breed")
    x_norm_5 = [500, 505]
    assert res_5.status_code <= x_norm_5[0] or res_5.status_code >= x_norm_5[1]
