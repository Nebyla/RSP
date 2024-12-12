import socket
from threading import Thread
from collections import deque

MULTICAST_GROUP = '233.0.0.1'
PORT = 1502
BUFFER_SIZE = 5
TCP_PORT = 12345  # Фиксированный порт для TCP-сервера

class IntermediateClient:
    def __init__(self):
        self.messages = deque(maxlen=BUFFER_SIZE)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', PORT))
        group = socket.inet_aton(MULTICAST_GROUP)
        mreq = group + socket.inet_aton('0.0.0.0')
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    
    def start(self):
        Thread(target=self.receive_messages).start()
        Thread(target=self.start_tcp_server).start()
    
    def receive_messages(self):
        last_message = ""
        while True:
            data, _ = self.sock.recvfrom(1024)
            message = data.decode()
            if message != last_message:
                print(f"New message: {message}")
                self.messages.append(message)
                last_message = message

    def start_tcp_server(self):
        tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server.bind(('localhost', TCP_PORT))  # Используем фиксированный порт TCP_PORT
        tcp_server.listen(1)
        print(f"TCP server running on port {TCP_PORT}")
        
        while True:
            client_sock, _ = tcp_server.accept()
            client_sock.sendall('\n'.join(self.messages).encode())
            client_sock.close()

if __name__ == "__main__":
    client = IntermediateClient()
    client.start()