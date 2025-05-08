#!/usr/bin/python3
"""
use of post
"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    r = requests.get(url, data={'email': email})
    print(r.text)
