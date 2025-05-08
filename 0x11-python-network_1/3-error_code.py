#!/usr/bin/python3
"""
handling error code
"""
import urllib.request
import sys
from urllib.error import HTTPError, URLError

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except HTTPError as e:
        print(f"Error code: {e.reason}")
