#!/bin/bash
# send a req json file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
