#!/bin/bash
# get req and display the req code 
curl -s -o /dev/null -w "%{http_code}" "$1"
