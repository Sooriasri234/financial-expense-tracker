import smtplib
from email.mime.text import MIMEText

def send_budget_alert(
    receiver_email,
    subject,
    body
):

    sender_email = "sooriasrikumararaja@gmail.com"

    app_password = "lagp ppvq qvvp bjxv"

    msg = MIMEText(body)

    msg['Subject'] = subject
    msg['From'] = "sooriasrikumararaja@gmail.com"
    msg['To'] = "sooriasri1964@gmail.com"

    try:

        server = smtplib.SMTP(
            'smtp.gmail.com',
            587
        )

        server.starttls()

        server.login(
            sender_email,
            app_password
        )

        server.sendmail(
            sender_email,
            receiver_email,
            msg.as_string()
        )

        server.quit()

        return True

    except Exception as e:

        print(e)

        return False