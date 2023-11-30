#!/bin/bash
# show the allow methods of http using curl 
curl -sI "$1" | grep Allow  | cut -d " " -f 2-
