import imaplib
import email
import os
from dotenv import load_dotenv
import time


def form_message_n_ticket(id):
    _, data = mail.uid('fetch', id, "(RFC822)")

    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)

    # Extract the message text
    subject = email_message["Subject"]

    ticket_id = subject[9:-8]

    message = ""
    if email_message.is_multipart():
        for part in email_message.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain":
                message += part.get_payload()
    else:
        message = email_message.get_payload()

    return message, ticket_id


if __name__ == "__main__":
    load_dotenv()

    # Connect to the email server
    mail = imaplib.IMAP4_SSL(host=str(os.getenv("IMAP_HOST")), port=int(os.getenv("IMAP_PORT")))
    mail.login(user=str(os.getenv("EMAIL_LOGIN")), password=str(os.getenv("PASSWORD_FOR_APP")))  # Password_for_app is a Google feature for people with 2-step verification account

    while True:
        mail.select("inbox")

        _, data = mail.uid('search', '(UNSEEN)', '(SUBJECT "[Ticket #" SUBJECT "] Mailer")')

        ids_mailer = data[0].split()
        print(ids_mailer)

        _, data = mail.uid('search', '(UNSEEN)', '(SUBJECT "New message from ")')  # Due to the big amount of messages in error_request.log will be only logged messages with "New message from "

        ids_other = data[0].split()
        print(ids_other)

        for id in ids_mailer:
            message, ticket_id = form_message_n_ticket(id)
            with open("success_request.log", "a") as f:
                f.write(f"Ticket ID: {ticket_id}\n")
                f.write(f"Message: {message}\n\n")
            # Mark the email as read
            mail.store(id, "+FLAGS", "\\Seen")

        for id in ids_other:
            message, _ = form_message_n_ticket(id)
            with open("error_request.log", "a") as f:
                f.write(f"{message}\n\n")
            # Mark the email as read
            mail.store(id, "+FLAGS", "\\Seen")

        # Wait for new emails
        time.sleep(10)
