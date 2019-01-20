# ftpClient
This is a simple project involves creation of a FTPClient with Python libraries like ftplib and tkinter similar to what FileZilla. 

Theory:
The File Transfer Protocol (FTP) is a standard network protocol used for the transfer of computer files between a client and server on a computer network.FTP users may authenticate themselves with a clear-text sign-in protocol, normally in the form of a username and password, but can connect anonymously if the server is configured to allow it. 
	
In cryptography, plaintext or cleartext is unencrypted information, as opposed to information encrypted for storage or transmission. Plaintext usually means unencrypted information pending input into cryptographic algorithms, usually encryption algorithms. Cleartext usually refers to data that is transmitted or stored unencrypted ('in the clear').

For secure transmission that protects the username and password, and encrypts the content, FTP is often secured with SSL/TLS (FTPS) or replaced with SSH File Transfer Protocol (SFTP).

An explanation of the the FTP is given here : https://www.youtube.com/watch?v=7v3GDgvdWO4

The default port on which the server listens is 21.
There are two separate channels which is used for file transfer :
  1. Control Channel - Used for authorization and browsing directory.Open while the connection is connected.
  2. Transfer Channel - Used for file transfer. Closed when the transfer is over.
Both are separate TCP channels.






