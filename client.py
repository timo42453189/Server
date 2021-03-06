import socket
import threading
import RPi.GPIO as GPIO
import time


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.178.78", 55555))

def device():
	while True:
		try:
			command = ""
			command = client.recv(1024).decode("ascii")
			print(command)
			if command == "ON":
				GPIO.setmode(GPIO.BCM)
				GPIO.setup(18, GPIO.OUT)
				GPIO.output(18, GPIO.HIGH)
				print('Successfully set pin 18 up!')
				time.sleep(3)
				GPIO.output(18, GPIO.LOW)
				print('Successfully set pin 18 down!')
				GPIO.cleanup()
		except:
			print("ERROR")
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
	if type == "DEVICE":		
		device()
	else:
		user()



handle()
