import smtplib, os, ssl


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    username = 'developmentandrzejr@gmail.com'
    password = os.environ['PMCGooglePass']
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as smtp:
        smtp.login(username, password)
        smtp.sendmail(username, username, message)
