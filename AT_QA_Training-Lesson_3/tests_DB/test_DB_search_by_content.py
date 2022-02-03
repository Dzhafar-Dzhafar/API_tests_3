import requests


def test_get_response_json_contents_6_search_by_content():
    response_1 = requests.get("https://www.openbrewerydb.org/page-data/projects/page-data.json")
    response_body_1 = response_1.json()
    abc = {'title': 'Add Project', 'url': '#add-project'}
    assert abc in response_body_1['result']['data']["mdx"]["tableOfContents"]['items']
