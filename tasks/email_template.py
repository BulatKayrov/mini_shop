from email.message import EmailMessage
from config import settings


def create_email(email_to: str):
    msg = EmailMessage()
    msg['Subject'] = "Subject: Подтверждение"
    msg['From'] = settings.EMAIL_HOST_USER
    msg['To'] = email_to
    msg.set_content('Просто контент!')
    return msg
