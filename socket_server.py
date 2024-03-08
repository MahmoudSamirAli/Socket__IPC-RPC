import socket

def server():
    # Get the hostname of the server
    host = socket.gethostname()
    # Get the ip
    IP = socket.gethostbyname(host)
    # Specify the port to listen on
    port = 21042
    # Create a socket object
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    # Bind the socket to the host and port
    s.bind((IP, port))
    # Listen for incoming connections, allowing up to 2 clients in the queue
    s.listen(3)
    # Accept an incoming connection
    while True : 
        print("===========================")
        print("the server is ready to accept clients")
        c, address = s.accept()
        print(f"Connected to: {address}")
        while True:
            # POLLING till Receive data from the client (up to 1024 bytes) and decode it
            data = c.recv(1024).decode()
            # If no data is received, break the loop
            if data == "end":
                print(f"the client {address} end the session")
                break
            print(f"Client {address} sent : {data}")
            # Get user input and send it to the client after encoding
            response = input(f"Enter response to send to client {address}: ")
            c.send(response.encode())
                        # Close the client connection
        c.close()
if __name__ == "__main__":
    # Start the server
    server()
