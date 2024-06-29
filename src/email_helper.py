import base64
import os
from email.message import EmailMessage

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def send_email_notification(to: str, subject:str, message: str):
    creds = None
    cred_filepath = "creds.json"
    token_filepath = "token.json"
    if os.path.exists(token_filepath):
        creds = Credentials.from_authorized_user_file(token_filepath, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(cred_filepath, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_filepath, 'w') as token:
            token.write(creds.to_json())

    try:
        service = build("gmail", "v1", credentials=creds)

        email_message = EmailMessage()

        email_message.set_content(message)

        email_message["To"] = to
        email_message["From"] = "insert_email_here"
        email_message["Subject"] = subject

        # encoded message
        encoded_message = base64.urlsafe_b64encode(email_message.as_bytes()).decode()

        create_message = {"raw": encoded_message}
        # pylint: disable=E1101
        send_message = (
            service.users()
            .messages()
            .send(userId="me", body=create_message)
            .execute()
        )
        print(f'Message Id: {send_message["id"]}')

    except HttpError as error:
        print(f"An error occurred: {error}")
        send_message = None

    return send_message

if __name__ == '__main__':
    temp = "98.6F"
    subject = "Fish tank temperature warning: {}".format(temp)
    message = "This is an automated message to let you know the fish tank has reached a temperature of {}.".format(temp)
    send_email_notification(to="4109672229@msg.fi.google.com", subject=subject, message=message)
    send_email_notification(to="tblattner@gmail.com", subject=subject, message=message)