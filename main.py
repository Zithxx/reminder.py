import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 1. Setup credentials from GitHub Secrets
gmail_user = os.environ['GMAIL_USER']      # Your Gmail address
gmail_password = os.environ['GMAIL_APP_PASS'] # The 16-character App Password
to_number = os.environ['MY_PHONE_NUMBER']  # 9 digits, e.g., 91xxxxxxx

# 2. Vodafone Portugal Gateway
carrier_gateway = "@sms.vodafone.pt"
sms_gateway = f"{to_number}{carrier_gateway}"

# 3. Message with the Image Link
# This uses the image we hosted yesterday
image_url = "https://i.postimg.cc/NFmkX9LC/1768346889340.png"
message_text = f"Reminder: Take your vitamins! 💊\nYou have a surprise here: {image_url}"

msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = sms_gateway
msg['Subject'] = "Vitamin Reminder" # Some gateways require a subject to pass filters

msg.attach(MIMEText(message_text, 'plain'))

# 4. Send the Email-to-SMS
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, sms_gateway, msg.as_string())
    server.quit()
    print(f"Success! Message sent to {sms_gateway}")
except Exception as e:
    print(f"Failed to send: {e}")
