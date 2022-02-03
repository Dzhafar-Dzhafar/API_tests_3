import requests


def test_get_response_json_contents_population_elements():
    response = requests.get("https://www.openbrewerydb.org/page-data/projects/page-data.json")
    response_body = response.json()
    assert len(response_body['result']['data']["mdx"]["tableOfContents"]['items']) == 7
