import socket
from threading import Thread

class EscapeRoomClient:
    def __init__(self, host='localhost', port=5558):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

        thread = Thread(target=self.listen_for_messages)
        thread.start()

        self.send_message()

    def send_message(self):
        while True:
            message = input()
            self.client.send(message.encode())

    def listen_for_messages(self):
        while True:
            try:
                msg = self.client.recv(1024).decode()
                if msg:
                    print(msg)
            except:
                print("Conexão encerrada.")
                self.client.close()
                break
