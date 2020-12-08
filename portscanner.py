#!/usr/bin/env python3
import sys
import socket



def get_accessible_ports(address, min_port, max_port):
	s = socket.socket()
	found_ports = []
	refused=[]
	for x in range(min_port,max_port+1):
		if s.connect_ex((address, x)):
			refused.append(x)
		else:
			found_ports.append(x)
			
	return found_ports

def main(argv):
	address = sys.argv[1]
	min_port = int(sys.argv[2])
	max_port = int(sys.argv[3])
	ports = get_accessible_ports(address, min_port, max_port)
	for p in ports:
		print(p)

# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 4:
		print('usage: python %s address min_port max_port' % sys.argv[0])
	else:
		main(sys.argv)
