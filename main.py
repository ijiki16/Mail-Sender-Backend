import ssl
import smtplib
from string import Template
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sendmail")
def send_mail():
    smtp_server = "smtp.gmail.com"
    port = 587

    sender_email = "testmail@gmail.com"
    sender_password = "testMailPassword"

    receiver_email = "demo@gmail.com"
    message = 'Message Text!!!'

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, sender_password)

        server.sendmail(sender_email, receiver_email, message)

        return {"Message": "Mail has been sent."}
    except Exception as e:
        print(e)
        return {"Message": "Error occurred while sending mail."}
    finally:
        server.quit()
