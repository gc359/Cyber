import socket

# create a new socket object
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set the default timeout for the socket object
socket.setdefaulttimeout(1)

# define the target server's IP address and port number
addr = "192.168.1.100"
port = 80
#you can find additional ports on your computer by going to the cmd typing this command 'netstat -ano'
#without the ''


# try to connect to the target server's IP address and port number
result = socket_obj.connect_ex((addr, port))

# close the socket object
socket_obj.close()

# print the scan result
if result == 0:
    print(f"Port {port} is open on {addr}")
else:
    print(f"Port {port} is closed on {addr}")

'''
TCP Scan
To overcome the demerits of echo request method, TCP scan method is introduced which works on three-way handshake method. This method has a pre-assumption that the hosts on the networks are open ports and we have to guess which port is open or not. The ports differ in the operating system in which you are using. Different OS has open dependent ports listed below.

linux: [20, 21, 22, 23, 25, 80, 111, 443, 445, 631, 993, 995]
windows: [135, 137, 138, 139, 445]
mac: [22, 445, 548, 631]
3-way-Handshake method
A three-way handshake is a method used in a TCP/IP network to create a connection between a local host/client and server. It is a three-step method that requires both the client and server to exchange SYN and ACK (acknowledgment) packets before actual data communication begins.
A three-way handshake is primarily used to create a TCP socket connection. It works when:

A client node sends an SYN data packet over an IP network to a server on the same or an external network. The objective of this packet is to ask/infer if the server is open for new connections.
The target server must have open ports that can accept and initiate new connections. When the server receives the SYN packet from the client node, it responds and returns a confirmation receipt – the ACK packet or SYN/ACK packet.
The client node receives the SYN/ACK from the server and responds with an ACK packet.
Upon completion of this process, the connection is created and the host and server can communicate.
'''

'''
Sources: https://www.geeksforgeeks.org/network-scanner-in-python/
'''