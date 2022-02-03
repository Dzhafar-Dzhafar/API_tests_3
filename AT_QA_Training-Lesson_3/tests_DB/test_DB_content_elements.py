import requests


def test_get_response_json_contents():
    response = requests.get("https://www.openbrewerydb.org/page-data/projects/page-data.json")
    response_body = response.json()
    assert response_body['result']['data']["mdx"]["tableOfContents"]['items'] == [
                        {
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
                        },
                        {
                            "url": "#java",
                            "title": "Java",
                            "items": [
                                {
                                    "url": "#java-api-client",
                                    "title": "Java API client"
                                },
                                {
                                    "url": "#openbrewery",
                                    "title": "OpenBrewery"
                                }
                            ]
                        },
                        {
                            "url": "#javascript",
                            "title": "JavaScript",
                            "items": [
                                {
                                    "url": "#beer-me",
                                    "title": "Beer Me"
                                },
                                {
                                    "url": "#brewtalk",
                                    "title": "BrewTalk"
                                },
                                {
                                    "url": "#graphql-server-nestjs",
                                    "title": "GraphQL Server (NestJS)"
                                },
                                {
                                    "url": "#lager-than-life",
                                    "title": "Lager Than Life"
                                },
                                {
                                    "url": "#local-brew",
                                    "title": "Local Brew"
                                },
                                {
                                    "url": "#open-brewery-react-app",
                                    "title": "Open Brewery React App"
                                }
                            ]
                        },
                        {
                            "url": "#net",
                            "title": ".NET",
                            "items": [
                                {
                                    "url": "#graphql-server-net-core",
                                    "title": "GraphQL Server (.NET Core)"
                                }
                            ]
                        },
                        {
                            "url": "#python",
                            "title": "Python",
                            "items": [
                                {
                                    "url": "#python-api-wrapper",
                                    "title": "Python API wrapper"
                                }
                            ]
                        },
                        {
                            "url": "#swift",
                            "title": "Swift",
                            "items": [
                                {
                                    "url": "#openbrewerykit",
                                    "title": "OpenBreweryKit"
                                }
                            ]
                        },
                        {
                            "url": "#add-project",
                            "title": "Add Project"
                        }
                    ]
