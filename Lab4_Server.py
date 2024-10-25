import socket
import time

MULTICAST_GROUP = '233.0.0.1'
PORT = 1502
FILE_PATH = 'message.txt'

def read_message():
    with open(FILE_PATH, 'r') as file:
        return file.read().strip()

def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)
    
    while True:
        message = read_message()
        sock.sendto(message.encode(), (MULTICAST_GROUP, PORT))
        print(f"Sent message: {message}")
        time.sleep(10)

if __name__ == "__main__":
    server()