import smtplib

def send_email_alert(msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("your_email@gmail.com", "app_password")

    server.sendmail(
        "from@gmail.com",
        "to@gmail.com",
        f"Subject: IoT ALERT\n\n{msg}"
    )