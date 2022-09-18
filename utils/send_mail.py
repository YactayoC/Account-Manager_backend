from email.message import EmailMessage
import ssl
import smtplib
import os

def sendMail(email_receiver: str, uid: str, fullname: str):
    email_sender = "proyectos.yactayo@gmail.com"
    email_password = os.getenv("EMAIL_PASSWORD")
    email_receiver = email_receiver

    subject = "Check your account"
    body = f"""
        Hello {fullname}, we sent you this email so you can verify your account through this link: http://127.0.0.1:5173/auth/confirm?uid={uid}.
        If it was not you, you can ignore this email.
    """

    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())