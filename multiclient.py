import socket
import threading

HOST = '127.0.0.1'
PORT = 55557

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(msg)
        except:
            print("Error! Connection closed.")
            client.close()
            break

def write():
    while True:
        msg = f'{nickname}: {input("")}'
        client.send(msg.encode('utf-8'))

threading.Thread(target=receive).start()
threading.Thread(target=write).start()
