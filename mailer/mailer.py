import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mailer:
    def __init__(self, server, port, sender_email, sender_pass):
        self.senderEmail = sender_email
        self.server = smtplib.SMTP(server, port)
        self.server.starttls()
        self.server.login(sender_email, sender_pass)
    
    def sendMail(self, sender_email, receiver_email, subject, body):
        # Construct the content
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        try:
            # Send the email
            self.server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Mail sent successfully!")
            
        except Exception as e:
            print(f"An error occured: {e}")
    