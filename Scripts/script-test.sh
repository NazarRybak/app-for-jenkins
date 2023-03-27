#! /bin/bash


response=$(curl -s http://127.0.0.1:5000)
if [ "$response" = "Hello, thats my little web-app!" ]; then
	echo "TRUE"
else 
	echo "FALSE"
fi
