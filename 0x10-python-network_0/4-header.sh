#!/bin/bash
#takes in a URL, sends a GET request to the URL and displays the response body
curl -sH "X-School-User-Id: 98" "$1"
