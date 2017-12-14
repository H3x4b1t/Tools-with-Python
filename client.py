import socket

servidor = "127.0.0.1"
puerto = 443

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((servidor, puerto))
cliente.send("HOLA SERVIDOR")
respuesta = cliente.recv(4096)
print respuesta