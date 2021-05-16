from flask import Flask , render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sendEmail')
def sendEmail():

    msg = MIMEMultipart()
    msg['Subject'] = 'Hello from Group#13'

    body = '''Hello
This is a test email sent from phython and flask

Thanks and Best Regards
Group 13 MMW'''
    msg.attach(MIMEText(body,'plain'))

    text = msg.as_string()

    email="touseef.ashraf90@gmail.com"
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("rajafaseehuzz@gmail.com","ykkxpkkoftsvgifp")
    response = server.sendmail("rajafaseehuzz@gmail.com",email,text)
    return "Email sent successfully!!!!"
    