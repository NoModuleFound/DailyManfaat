PRIVATE_KEY="certs/jwt-private.pem"
PUBLIC_KEY="certs/jwt-public.pem"

mkdir -p certs

if [ ! -f "$PRIVATE_KEY" ]; then
    echo "Private key not found. Generating a new RSA key..."
    openssl genpkey -algorithm RSA -out "$PRIVATE_KEY"
    chmod 600 "$PRIVATE_KEY"
else
    echo "Private key exists."
fi


if [ ! -f "$PUBLIC_KEY" ]; then
    echo "Public key not found. Generating from the private key..."
    openssl rsa -in "$PRIVATE_KEY" -pubout -out "$PUBLIC_KEY"
else
    echo "Public key exists."
fi

echo "Done."
