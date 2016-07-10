import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print "Faild to create socket: Error code (" + str(msg[0]) + ") Error msg: " + msg[1]
    sys.exit()

print "Socket created"


hostname = raw_input("Enter a hostname: ")
port = int(raw_input("Enter a port: "))

try:
    remote_ip = socket.gethostbyname(hostname)
except socket.gaierror:
    print "Hostname %s could not be resolved" % hostname
    sys.exit()

print "Ip address of hostname %s is %s" % (hostname, remote_ip)

s.connect((remote_ip, port))

print "Socket connected to " + hostname + " on ip " + remote_ip

message = "GET / HTTP/1.1\r\n\r\n"

try:
    print s.sendall(message)
except socket.error:
    print "Send failed"
    sys.exit()
print "send successfully"

reply = s.recv(4096)

print reply

s.close()
    
