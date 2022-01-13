def test_answer(url_param):
    if url_param == "https://dog.ceo/api/breed/hound/list":
        print("Породы:")
    elif url_param == "https://dog.ceo/api/breed/hound/":
        print("перейдите в /list!")
    elif url_param == "https://dog.ceo/api/breed/":
        print("перейдите в /hound/list!")
    elif url_param == "https://dog.ceo/api/":
        print("перейдите в /breed/hound/list!")
    elif url_param == "https://dog.ceo/":
        print("перейдите в /api/breed/hound/list!")
    else:
        print("Вы находитесь в начале пути (https://dog.ceo)___/api/breed/hound/list")
