#!/bin/sh

echo "Content-Type: text/html"
echo ""

urldecode() {
   printf '%b' "$(echo "$1" | sed 's/+/ /g; s/%/\\x/g')"
}

get_param() {
   echo "$QUERY_STRING" |
      tr '&' '\n' |
      grep "^$1=" |
      head -n 1 |
      cut -d= -f2-
}

ID="$(urldecode "$(get_param id)")"
CUSTOMER_ID="$(urldecode "$(get_param customer_id)")"
CHANNELS="$(urldecode "$(get_param channels)")"
IGUANAX="$(urldecode "$(get_param iguanax)")"

if [ ! -d "/home/eliot/customers/$ID" ]; then
    echo "<html><body>"
    echo "<h3>License not issued</h3>"
    echo "<pre>"
    echo "Unknown customer ID: $ID"
    echo "</pre>"
    echo "</body></html>"
    exit 1
fi

echo "<html><body>"
echo "Iguana License Key"
echo "<pre>"

echo "ID=$ID"
echo "CUSTOMER_ID=$CUSTOMER_ID"
echo "CHANNELS=$CHANNELS"
echo "IGUANAX=$IGUANAX"
echo 

if [ "$IGUANAX" = "true" ]; then
/home/eliot/iguanax/IguanaLicense/IguanaLicense "$ID" "$CHANNELS" "$CUSTOMER_ID"
else
/home/eliot/iguana6/IguanaLicense/IguanaLicense "$ID" "$CHANNELS" "$CUSTOMER_ID"
fi

echo "</pre>"
echo "</body></html>"
