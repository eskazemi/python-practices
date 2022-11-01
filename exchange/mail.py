import smtplib
import requests

# from config import EMAIL_RECEIVER
# from local_config import MAILGUN_APIKEY

from email.mime.text import MIMEText


# def send_api_email(subject, body):
#     return requests.post(
#         "https://api.mailgun.net/v3/inprobes/messages",
#         auth=("api", MAILGUN_APIKEY),
#         data={
#             "from": "Hosein finance@inprobes.com",
#             "to": ["hs.ramezanpoor@gmail.com", "hosein@inprobes.com"],
#             "subject": subject,
#             "text": body
#         }
#     )

#
# def send_smtp_email(subject, body):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = "finance@inprobes.com"
#     msg['To'] = EMAIL_RECEIVER
#
#     with smtplib.SMTP('smtp.mailgun.org', 587) as mail_server:
#         mail_server.login('postmaster@mg.inprobes.com', MAILGUN_APIKEY)
#         mail_server.sendmail(msg['From'], msg['To'], msg.as_string())
#         # mail_server.quit()
