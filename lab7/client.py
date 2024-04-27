import os
from dotenv import load_dotenv
import socket


def send_email():
    while True:
        load_dotenv()
        email = input("Enter your email address: ")
        message = input("Enter your message: ")

        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        s.connect(("127.0.0.1", 1))

        # Send email and message to the server
        s.sendall(f"{email}\n{message}".encode())

        # Receive response from the server
        response = s.recv(1024).decode()

        # Check if the response is OK
        if response == "OK":
            print("Email sent successfully!")
            break
        elif response:
            print(f"Error: {response}")
        else:
            print("Response from server had not been sended!")

    # Close the socket
    s.close()


if __name__ == "__main__":
    send_email()
