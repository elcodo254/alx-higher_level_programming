#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""
import sys
import requests


if __name__ == "__ main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    req = requests.post(url, data=value)
    print(req.text)
