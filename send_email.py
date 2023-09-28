import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv  # pip intall python-dotenv

PORT = 587
EMAIL_SERVER = "smtp-mail.outlook.com"

# Load the environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")

def send_email(subject, receiver_email,):
    # Create the base text message.
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Gotham Pearl Labs", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        Hi Rod,
        This is an initial test.
        """  
    )

    # Add the HTML version. This converts the message into a multipart/alternative container.
    msg.add_alternative(
        f"""\
        <html>
            <body>
                <p>Hi Rod,</p>
                <p>This is an initial test.</p>
            </body>
        </html>
        """,
        subtype="html",
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ == "__main__":
    send_email(
        subject="CSP Bi-Weekly Accomplishments",
        receiver_email="sambamjalloh@gmail.com",
    )
        




