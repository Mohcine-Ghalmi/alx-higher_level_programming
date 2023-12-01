#!/usr/bin/python3
"""
time
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    req = requests.get(url)
    commits = req.json()

    try:
        for index in range(10):
            print("{}: {}".format(
                commits[index].get("sha"),
                commits[index].get("commit").get("author").get("name")))
    except IndexError:
        pass
