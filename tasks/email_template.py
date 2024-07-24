import uuid
from email.message import EmailMessage
from config import settings


def create_email(email_to: str):
    msg = EmailMessage()
    msg['Subject'] = "Subject: Подтверждение"
    msg['From'] = settings.EMAIL_HOST_USER
    msg['To'] = email_to
    msg.set_content(f'http://127.0.0.1:8000/api/auth/{uuid.uuid4} перейдите по ссылке')
    return msg
