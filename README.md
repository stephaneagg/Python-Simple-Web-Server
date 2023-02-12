# Simple-Web-Server
Simple web server with written in Python using the Socket and Select modules to support both persistent and non-persistent HTTP connections with limited timeout capabilities. 

Py files in sws.py and client.py

sws.py is the simple web server. To start the server, enter "python3 sws.py <IP_ADDRESS> <PORT_NUMBER>" in the terminal.

client.py is a program that was used to test sws.py. This program takes input from the terminal and sends them as requests to sws.py. To run client.py enter "python3 client.py <IP_ADDRESS> <PORT_NUMBER>" in the terminal.

Once sws.py is running and client.py has been connected, requests can be sent through clien.py.
sws.py accepts requests of the form

GET /<filename> HTTP/1.0\n
Connection:<close or keep-alive>\n
\n

the GET line is the only manditory line. If connection is not specified a non-persistent connection is assumed.
Two new lines after input will be accepted as a request.

Responses from the server include 404 NOT FOUND, 400 BAD REQUEST, 200 OK.
  
The following is a sample input and output of SWS.py

INPUT
  GET /small.html HTTP/1.0\n
  Connection:keep-alive\n
  \n

RESPONSE
  HTTP/1.0 200 OK

  Connection: Keep-alive

  Transmission correct!
