#!/bin/zsh

openssl genrsa -out private_key.pem 4096
openssl rsa -in private_key.pem -pubout -out public_key.pem

# Ed25519
# ssh-keygen -t ed25519 -C "your_email@example.com" -f ./ed25519_key