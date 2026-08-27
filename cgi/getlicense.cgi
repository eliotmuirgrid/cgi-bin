#!/bin/sh

INSTANCEID="$(printf '%s' "$QUERY_STRING" |
    tr '&' '\n' |
    sed -n 's/^instanceid=//p')"

printf 'Status: 302 Found\r\n'
printf 'Location: https://license.interfaceware.com/license?id=%s&customer_id=sdfs&channels=5&iguanax=false\r\n' "$INSTANCEID"
printf '\r\n'
