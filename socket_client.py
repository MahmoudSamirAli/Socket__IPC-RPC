# ​ Import the socket module
import socket
def client():
    # Get the host name (as both server and client code are running on your PC)
    host = socket.gethostname()
    # Get the ip
    IP = socket.gethostbyname(host)
    # Define the server's port number to interact with
    port = 21042
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    # Connect to the server by specifying the hostname and port number
    client_socket.connect((IP, port))
    # printing my socket address
    print (f"my socket is : {client_socket.getsockname()[:]}")
    while True :
        # Prompt the user for input
        message = input("Enter your message (Type 'end' to exit): ")
        if message.lower().strip() == "end" :
            # Send the message to the server
            client_socket.send(message.encode())
            # Close the connection
            break 
        # Send the message to the server
        client_socket.send(message.encode())
        # POLLING till Receive a response from the server
        data = client_socket.recv(1024).decode()
        # Display the received message from the server
        print("Received from server: " + data)
    client_socket.close()

if __name__ == "__main__":
    client()
