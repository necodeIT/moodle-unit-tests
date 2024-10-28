# import requests as r
from packaging.version import parse


# def get_releases(depth: int = 1) -> list[str]:
#     tags = []
#     url = "https://hub.docker.com/v2/repositories/bitnami/moodle/tags?page_size=100"
#     page = 0

#     while url is not None and page < depth:
#         response = r.get(url)
#         response.raise_for_status()
#         data = response.json()

#         tags.extend(
#             tag["name"]
#             for tag in data["results"]
#             if not tag["name"].startswith("sha")
#             and "debian" not in tag["name"]
#             and tag["name"] != "latest"
#         )

#         url = data.get("next")
#         page += 1

#     sorted_tags = sorted(tags, key=parse, reverse=True)

#     return ["latest"] + sorted_tags


def get_releases(depth: int = 1) -> list[str]:
    return ["latest", "4.3.7", "3.11.11"]
