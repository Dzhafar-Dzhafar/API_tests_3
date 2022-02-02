def test_url_for_coincidences(url_params):
    if url_params == "https://dog.ceo/api/breed/hound/list":
        print("Породы:")


def test_url_for_coincidences_1(url_params):
    if url_params == "https://dog.ceo/api/breed/hound/":
        print("перейдите в /list!")


def test_url_for_coincidences_2(url_params):
    if url_params == "https://dog.ceo/api/breed/":
        print("перейдите в /hound/list!")


def test_url_for_coincidences_3(url_params):
    if url_params == "https://dog.ceo/api/":
        print("перейдите в /breed/hound/list!")


def test_url_for_coincidences_4(url_params):
    if url_params == "https://dog.ceo/":
        print("перейдите в /api/breed/hound/list!")
