import random, os
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = "your_email"
MAIL_PASSWORD = "your_password"

NAME = ["name1", "name2", "name3"]
EMAIL = ["fakeemail1", "fakeemail2", "fakeemail3"]

app.config['MAIL_SERVER'] = MAIL_SERVER
app.config['MAIL_PORT'] = MAIL_PORT
app.config['MAIL_USE_TLS'] = MAIL_USE_TLS
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD

mail = Mail(app)

def generator(name, email):
    zip_iterator = zip(name, email)
    santa_dict = dict(zip_iterator)

    giver = name.copy()
    receiver = name.copy()

    different = False
    while different is not True:
        different = True
        random.shuffle(receiver)

        for i in range(len(giver)):
            if giver[i] == receiver[i]:
                different = False
            
        if different is True:
            send_mail(santa_dict, giver, receiver)

def send_mail(santa_dict, giver, receiver):

    for i in range(len(santa_dict)):
        msg_subject = "SECRET SANTA CO."
        msg = Message(
            msg_subject,
            sender=("SECRET SANTA CO.",  MAIL_USERNAME),
            recipients=[santa_dict.get(giver[i])]
        )
        msg.html = "<p>Hello <b>" + giver[i] + ",</b></p>"
        msg.html += "<p>You are to gift: " + receiver[i] + ".</b></p>"
        # msg.html += '<img src="https://www.theplace2.ru/archive/megan_fox/img/96176036.jpg">'
        msg.html += "<p>Created by @ehandywhyy in Github</b></p>"
        mail.send(msg)

@app.route("/")
def index():
    generator(NAME, EMAIL)
    return "Email has been sent."

if __name__ == '__main__':
   app.run(debug = True)



    