import socket


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    PORT = 12345
    server.bind(('localhost', PORT))
    server.listen(1)

    print(f'Server at port {PORT}')
    print("Server is waiting for connection...")

    # クライアントからの接続を待機
    client, addr = server.accept()
    print("Connected by", addr)

    # クライアントからデータを受信
    data = client.recv(4096)
    print('===== クライアントからのメッセージ =====')
    # print(data)
    print(data.decode())
    print('=====================================')

    client.close()
    server.close()


if __name__ == '__main__':
    main()
