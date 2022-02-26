import smtplib

sender = "" # your email goes here
receiver = "" # the person who you are sending the email's address
password = "" # password of your google account
subject = "" # subject of the email goes here
body = "" # body of the email goes here

message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("Sorry! You are unable to sugn in")
