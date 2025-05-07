#!/bin/bash
# Script that takes in a URL, sends a GET request, and displays body only for status code 200
curl -s -o body.txt -w "%{http_code}" "$1" | grep -q "200" && cat body.txt
