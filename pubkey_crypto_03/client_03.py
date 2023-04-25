import socket

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


def main():
    server = ('localhost', 12345)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(server)

    # メッセージを作る(平文)
    message = input('> ').encode()

    # 事前に取得しておいた公開鍵
    with open('public_key.pem', 'rb') as public_file:
        public_key = RSA.import_key(public_file.read())

    # 公開鍵を使って送信したいデータを暗号化
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_data = cipher_rsa.encrypt(message)

    # 暗号化されたデータを送信する
    client.send(encrypted_data)

    client.close()


if __name__ == '__main__':
    main()
