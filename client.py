import socket
import threading


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("SERVER_ADDRESS", 55551))

def lamp():
	while True:
		try:
			command = client.recv(1024)
			print(command.decode("ascii"))
		except:
			break

def user():
	while True:
		try:
			command = input("Command: ")
			client.send(command.encode("ascii"))
		except:
			break

def handle():
	type = input("User (type in user name) or Lamp (type in LAMP)? ")
	message = client.recv(1024).decode("ascii")
	if message == "!USER":
		client.send(type.encode("ascii"))

	if type == "LAMP":		
		lamp()
	else:
		user()



handle()
