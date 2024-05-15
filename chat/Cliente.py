import socket
import threading

def send_message():
    """
    Envia mensagens para o servidor.
    """
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

def receive_message():
    """
    Recebe mensagens do servidor.
    """
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print(message)

# Configurações do cliente
HOST = '0.0.0.0'  # Endereço IP do servidor
PORT = 5555

# Cria o socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Inicia threads para enviar e receber mensagens
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)

send_thread.start()
receive_thread.start()
