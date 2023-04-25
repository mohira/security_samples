import socket

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


def main():
    with open('private_key.pem', 'rb') as private_file:
        private_key = RSA.import_key(private_file.read())

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    PORT = 12345
    server.bind(('localhost', PORT))
    server.listen(1)

    print(f'Server at port {PORT}')
    print("Server is waiting for connection...")

    # クライアントからの接続を待機
    client, addr = server.accept()
    print("Connected by", addr)

    # クライアントから暗号化されたデータを受信
    encrypted_data = client.recv(4096)
    print('\n===== クライアントからの暗号文 =====\n')
    print(encrypted_data)
    print('\n=====================================\n')

    # 秘密鍵でデータを復号
    cipher_rsa = PKCS1_OAEP.new(private_key)

    try:
        decrypted_data = cipher_rsa.decrypt(encrypted_data)
        print('\n===== クライアントからの平文(復号したメッセージ) =====\n')
        print(decrypted_data.decode())
        print('\n=====================================\n')
    except ValueError as e:
        print(f'Error: {e}')

    client.close()
    server.close()


if __name__ == '__main__':
    main()
