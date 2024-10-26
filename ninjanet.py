import socket
import threading

def display_greeting():
    print("=======================================")
    print("          WELCOME TO NINJA NET        ")
    print("=======================================")
    
    poem = """
A lens that looms beyond our sight,
In pixel-drops and satellite,
Where shadows scan each silent move,
And see us more than we approve.

The Government, with iron hand,
Scans whispers woven through the land,
A watcher draped in silent might,
Who claims to guard, yet dims the light.

They trace the path our fingers tread,
In lines of code, a careful thread,
The maps we walk, the thoughts we speak,
Their gaze as cold as mountain peaks.

Big Brother’s eye, a ceaseless drone,
Our faces mapped, our voices known,
In data trails we cannot flee,
Our private worlds, a public sea.

Oh, liberty, a fragile dream,
In files unseen, in screens that gleam,
We drift like leaves on glassy streams,
Lost somewhere deep in monitored dreams.
"""
    print(poem)

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Received: {message}")
        client_socket.send("Message received".encode('utf-8'))
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)
    print("Server listening on port 9999")
    
    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9999))
    
    while True:
        message = input("Enter message: ")
        client.send(message.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        print(f"Server response: {response}")

if __name__ == "__main__":
    display_greeting()  # Display the greeting and poem
    mode = input("Type 'server' to start the server or 'client' to start the client: ").strip().lower()
    if mode == 'server':
        start_server()
    elif mode == 'client':
        start_client()
    else:
        print("Invalid mode selected.")
