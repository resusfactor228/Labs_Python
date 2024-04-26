import imaplib
import email
import os
import time

# Connect to the email server
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("admin@example.com", "password")
mail.select("inbox")

while True:
    # Search for new emails with the specified subject format
    result, data = mail.search(None, "SUBJECT \"[Ticket #*] Mailer\"")
    ids = data[0].split()

    # Process each new email
    for id in ids:
        result, data = mail.fetch(id, "(RFC822)")
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)

        # Extract the ticket ID and message text
        subject = email_message["Subject"]
        ticket_id = subject[8:-7]
        message = ""
        if email_message.is_multipart():
            for part in email_message.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain":
                    message += part.get_payload()
        else:
            message = email_message.get_payload()

        # Write the ticket ID and message text to the success log file
        with open("success_request.log", "a") as f:
            f.write(f"Ticket ID: {ticket_id}\n")
            f.write(f"Message: {message}\n\n")

        # Mark the email as read
        mail.store(id, "+FLAGS", "\\Seen")

    # Wait for new emails
    time.sleep(int(os.getenv("PERIOD_CHECK")))
