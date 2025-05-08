#!/usr/bin/python3
"""
check status
"""
import urllib.request
"""fetch url"""
with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    body = response.read()
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
