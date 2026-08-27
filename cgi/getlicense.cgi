#!/bin/sh

printf "Content-Type: text/plain\r\n"
printf "\r\n"

echo "QUERY_STRING=$QUERY_STRING"
echo "REQUEST_METHOD=$REQUEST_METHOD"
echo "REMOTE_ADD=$REMOTE_ADDR"

