import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://dog.ceo/api/breed/hound/list",
        help="This is request url"
    )


@pytest.fixture
def url_param(request):
    return request.config.getoption("--url")


@pytest.fixture()
def default_url():
    return "https://dog.ceo/api"


@pytest.fixture()
def pic_url():
    return "breeds/image/random"
