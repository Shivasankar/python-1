import socket               

s = socket.socket()         
host = socket.gethostname() 
port = 8111
s.bind((host, port))
s.listen(5)           
while True:
   c, addr = s.accept() 
   #print 'Got connection from', addr
   print c.recv(1024)
   c.send('hello world from server')
   c.close()        
   
