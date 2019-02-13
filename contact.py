#!/usr/bin/python3.7

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask_mail import Mail, Message
import config as config

app = Flask(__name__)
app.secret_key = b''

app.config.update(dict(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS =  True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = config.credentials["email_address"],
    MAIL_PASSWORD = config.credentials["password"]
))

mail = Mail(app)

@app.route("/email", methods=["GET", "POST"])
def send_email():
    if request.method == 'POST':
        guest_addr = request.form.get('email')
        message = request.form.get('message')
        subject = request.form.get('subject') + ' from ' + guest_addr
        name = request.form.get('name')
        msg = Message(subject, sender=guest_addr, recipients=config.destination["recipient"], reply_to=guest_addr)
        msg.body = message + '\n\n From: %s' % guest_addr
        mail.send(msg)
    return redirect(config.redirect["redirect"])

if __name__ == '__main__':
    app.run(debug = False)
