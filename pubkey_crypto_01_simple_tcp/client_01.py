import socket


def main():
    server = ('localhost', 12345)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(server)

    message = input('> ').encode()
    # client.send(b"Hello, this is a secret message!")
    client.send(message)

    client.close()


if __name__ == '__main__':
    main()
