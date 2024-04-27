import os
from dotenv import load_dotenv
import socket
import smtplib
import time
import uuid
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re


def validate_email(email):
    # Validate email address using regular expression
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def send_mail(sender, recipient, subject, body):
    # Create a multipart message object
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject

    # Attach the body to the message
    message.attach(MIMEText(body))

    # Create a secure SMTP connection and send the message
    server = smtplib.SMTP(host=str(os.getenv("SMTP_HOST")), port=int(os.getenv("SMTP_PORT")))
    server.starttls()
    server.login(sender, os.getenv("PASSWORD_FOR_APP"))  # requires password of sender's account, but our sender is also recipient in both cases, so...
    text = message.as_string()
    server.sendmail(sender, recipient, text)
    server.quit()


def listen_for_messages():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to an address and port
    s.bind(("127.0.0.1", 1))

    # Listen for incoming connections
    s.listen(1)

    while True:
        # Accept an incoming connection
        connection, address = s.accept()

        # Receive email and message from the client
        data = connection.recv(1024).decode()
        email, message = data.split("\n")

        # Validate email address
        if not validate_email(email):
            connection.sendall("Invalid email address".encode())
            continue

        # Generate a unique ID for the ticket
        ticket_id = str(uuid.uuid4())

        # Send email to the user
        sender = os.getenv("EMAIL_LOGIN")
        subject = f"[Ticket #{ticket_id}] Mailer"
        send_mail(sender, email, subject, message)

        # Send email to the administrator
        sender = email
        subject = f"[Ticket #{ticket_id}]\n New message from {sender}\n"

        recipient = os.getenv("EMAIL_LOGIN")
        body = f"{email} wrote:\n\n{message}"

        send_mail(sender, recipient, subject, body)

        # Send OK response to the client
        connection.sendall("OK".encode())

        # Close the connection
        connection.close()


if __name__ == "__main__":
    load_dotenv()
    listen_for_messages()
