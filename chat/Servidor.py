import socket
import threading

def handle_client(client_socket, address):
    """
    Lida com as mensagens recebidas de um cliente.
    """
    while True:
        # Recebe a mensagem do cliente
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Mensagem de {address[0]}: {message}")
        # Envie a mensagem para todos os clientes, exceto para o remetente
        broadcast(message, client_socket)

def broadcast(message, sender_socket):
    """
    Envie a mensagem para todos os clientes, exceto para o remetente.
    """
    for client in clients:
        if client != sender_socket:
            client.send(message.encode('utf-8'))

# Configurações do servidor
HOST = '0.0.0.0'
PORT = 5555

# Cria o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"[*] Servidor escutando em {HOST}:{PORT}")

# Lista para armazenar todos os clientes conectados
clients = []

while True:
    # Aceita uma conexão de cliente
    client_socket, address = server_socket.accept()
    print(f"[*] Nova conexão de {address[0]}:{address[1]}")
    clients.append(client_socket)

    # Inicia uma nova thread para lidar com o cliente
    client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
    client_handler.start()
