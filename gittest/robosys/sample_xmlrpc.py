import xmlrpclib
server = xmlrpclib.Server('http://xmlrpc-c.sourceforge.net/api/sample.php')
result = server.sample.add(1,2)
print(result)
