import random
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = "your_email"
MAIL_PASSWORD = "your_password"

NAME = ["name1", "name2", "name3"]
EMAIL = ["email1", "email2", "email3"]
DEBUG_FLAG = True

app.config['MAIL_SERVER'] = MAIL_SERVER
app.config['MAIL_PORT'] = MAIL_PORT
app.config['MAIL_USE_TLS'] = MAIL_USE_TLS
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD

mail = Mail(app)

def generator(giver, email):
    santa_dict = dict(zip(giver, email))
    receiver = giver.copy()

    duplicate_flag = False
    while duplicate_flag is not True:
        duplicate_flag = True
        random.shuffle(receiver)

        for _, giver_name in enumerate(giver):
            if giver_name == receiver[_]:
                duplicate_flag = False
            
        if duplicate_flag is True:
            send_mail(santa_dict, receiver)

def send_mail(santa_dict, receiver):
    for _, (giver_name, giver_email) in enumerate(santa_dict.items()):
        msg_subject = "SECRET SANTA CO."
        msg = Message(
            msg_subject,
            sender=("SECRET SANTA CO.",  MAIL_USERNAME),
            recipients=[giver_email]
        )
        msg.html = "<p>Greetings " + giver_name + ",</p><br/>"
        msg.html += "<p>You are the secret santa to: <b><u>" + receiver[_] + "</u></b>.</p>"
        msg.html += "<p>The budget is maximum $20 :)</p>"
        # msg.html += '<img src="https://img.freepik.com/free-vector/gradient-christmas-tinsel-background_52683-76117.jpg">'
        msg.html += "<p>Created by <a href=\"https://github.com/xfortisfye\">@xfortisfye</a></p>"
        mail.send(msg)

@app.route("/")
def index():
    generator(NAME, EMAIL)
    return "Email has been sent without errors. Do remind your users to check their junk box."

if __name__ == '__main__':
   app.run(debug = True)



    