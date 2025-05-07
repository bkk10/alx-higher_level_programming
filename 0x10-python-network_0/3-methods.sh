#!/bin/bash
# Script that displays all HTTP methods the server will accept for a given URL
curl -sI -X OPTIONS "$1"
