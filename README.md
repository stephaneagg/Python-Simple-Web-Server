# Simple-Web-Server
Simple web server with written in Python using the Socket and Select modules to support both persistent and non-persistent HTTP connections with limited timeout capabilities. <br>

Py files in sws.py and client.py<br>

sws.py is the simple web server. To start the server, enter "python3 sws.py <IP_ADDRESS> <PORT_NUMBER>" in the terminal.<br>

client.py is a program that was used to test sws.py. This program takes input from the terminal and sends them as requests to sws.py. To run client.py enter "python3 client.py <IP_ADDRESS> <PORT_NUMBER>" in the terminal.<br>

Once sws.py is running and client.py has been connected, requests can be sent through clien.py.<br>

sws.py accepts requests of the form<br>

GET /(filename) HTTP/1.0\n<br>
Connection:(close or keep-alive)\n<br>
\n<br>

the GET line is the only manditory line. If connection is not specified a non-persistent connection is assumed.<br>
Two new lines after input will be accepted as a request.<br>

Responses from the server include 404 NOT FOUND, 400 BAD REQUEST, 200 OK.<br>
  
The following is a sample input and output of SWS.py<br>

INPUT<br>
  GET /small.html HTTP/1.0\n<br>
  Connection:keep-alive\n<br>
  \n

RESPONSE<br>
  HTTP/1.0 200 OK<br>

  Connection: Keep-alive<br>

  Transmission correct!<br>
