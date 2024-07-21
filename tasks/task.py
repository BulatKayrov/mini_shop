import smtplib

from config import settings
from tasks.celery_ import app
from tasks.email_template import create_email


@app.task
def send_message(email: str):
    content = create_email(email)

    with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
        server.ehlo()
        server.starttls()
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        server.send_message(from_addr=settings.EMAIL_HOST_USER, to_addrs=email, msg=content)
        server.quit()
