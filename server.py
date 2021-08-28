import socket
import threading

IP = "SERVER_IP"
PORT = 55551
ADDR = (IP, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print("Listening for new connections!")

lamps = []
users = []

def send(command, sender):
	command_decodet = command.decode("ascii")
#	if command_decodet == "ON" or command_decodet == "OFF":
	for lamp in lamps:
		lamp.send(command)
#	else:
#		sender.send("Invailed command".encode("ascii"))

def handle_users(client):
	while True:
		try:
			command = client.recv(1024)
			print(command.decode("ascii"))
			send(command, client)
		except:
			users.remove(client)
			client.close()
			print(f"User {client} disconnected")
			break


def connect():
	while True:
		client, address = server.accept()
		print(f"New connection with {address}")
		client.send("!USER".encode("ascii"))
		name = client.recv(1024)
		if name.decode("ascii") == "LAMP":
			lamps.append(client)
			print("New Lamp addet")
			client.send("Successfully addet lamp!".encode("ascii"))

		else:
			print("New User addet")
			users.append(client)
			thread = threading.Thread(target=handle_users, args=(client,))
			thread.start()

connect()
