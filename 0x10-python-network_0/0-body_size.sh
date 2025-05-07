#!/bin/bash
#script that takes in a url, sends a request to that url and displays the size of the body
curl -s -o /dev/null -w "%{size_download}\n" "$1"
