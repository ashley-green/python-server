import http.server
import socketserver

PORT = 8080


try:
    #Create a web server and define the handler to manage the
    #incoming request
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(('', PORT), Handler)
    print ('Started httpserver on port ' , PORT)

    #Wait forever for incoming htto requests
    httpd.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
