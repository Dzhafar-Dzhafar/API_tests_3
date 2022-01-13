import pytest


@pytest.fixture()
def default_url():
    return "https://dog.ceo/api"


@pytest.fixture()
def pic_url():
    return "breeds/image/random"
