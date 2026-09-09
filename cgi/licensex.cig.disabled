#!/bin/sh
cat <<'EOF'
Content-Type: text/html

EOF

KEY="$(printf '%s' "$QUERY_STRING" | sed 's/^id=//')"

echo "Iguana X License code.  This is for development purposes"
echo "<pre>"
/home/eliot/iguanax/IguanaLicense/IguanaLicense "$KEY"
echo "</pre>"
echo "Contact license@interfaceware.com for permanent licenses."


