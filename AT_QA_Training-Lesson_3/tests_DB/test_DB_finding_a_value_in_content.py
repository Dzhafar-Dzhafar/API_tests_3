import requests


def test_get_response_json_contents_0():
    response = requests.get("https://www.openbrewerydb.org/page-data/projects/page-data.json")
    response_body = response.json()
    assert response_body['result']['data']["mdx"]["tableOfContents"]['items'][0] == {
        "url": "#flutter",
        "title": "Flutter",
        "items": [
            {
                "url": "#hopyard-built-with-flutter",
                "title": "hopyard (built with Flutter)"
            },
            {
                "url": "#open-brewery-db-flutter-package",
                "title": "Open Brewery DB Flutter Package"
            }
        ]
    }


def test_get_response_json_contents_6():
    response_1 = requests.get("https://www.openbrewerydb.org/page-data/projects/page-data.json")
    response_body_1 = response_1.json()
    assert response_body_1['result']['data']["mdx"]["tableOfContents"]['items'][6] == {
        "url": "#add-project",
        "title": "Add Project"
    }
