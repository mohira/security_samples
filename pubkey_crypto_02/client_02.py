import socket

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


def main():
    server = ('localhost', 12345)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(server)

    # メッセージを作る
    message = input('> ').encode()
    # client.send(b"Hello, this is a secret message!")

    # サーバから公開鍵を受信
    public_key = client.recv(4096)

    # 公開鍵を使って送信したいデータを暗号化
    recipient_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    encrypted_data = cipher_rsa.encrypt(message)

    # 暗号化されたデータを送信する
    client.send(encrypted_data)

    client.close()


if __name__ == '__main__':
    main()
