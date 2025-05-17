import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

def send_birthday_email(name, email):
    from dotenv import load_dotenv
    load_dotenv()

    sender_email = os.getenv("GMAIL_USER")
    sender_pass = os.getenv("GMAIL_PASS")

    msg = MIMEMultipart()
    msg["Subject"] = f"🎉 Happy Birthday {name}!"
    msg["From"] = sender_email
    msg["To"] = email

    body = f"""
    <html>
      <body>
        <h2>Happy Birthday, {name}! 🎂</h2>
        <p style="font-size: 16px; line-height: 1.5; color: #333;">
          Today, the sun rises just for you, painting the sky with golden hues of joy to celebrate the most loved person in our hearts—you, {name}! Like a mighty oak tree standing tall through every season, your warmth and strength bring life to everyone around you. 🌳
          <br><br>
          May your year ahead bloom like a meadow of wildflowers, each petal bursting with happiness, love, and endless wonder. May your laughter ripple like a gentle stream through a forest, bringing peace to all who hear it. And may your dreams soar as high as an eagle, carried by the winds of hope and magic. 🦅
          <br><br>
          You are a rare and radiant star in our sky, {name}, shining brighter with every passing year. Here’s to a day as magnificent as a sunset over the ocean, and a life as boundless as the horizon. Wishing you a truly wondrous birthday filled with all the beauty of nature’s embrace! 🌅
        </p>
      </body>
    </html>
    """
    msg.attach(MIMEText(body, "html"))

    # Attach greeting card image
    with open("greeting_card.png", "rb") as f:
        img = MIMEImage(f.read(), name="greeting_card.png")
        msg.attach(img)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_pass)
            server.sendmail(sender_email, email, msg.as_string())
            print(f"✅ Email sent to {email}")
    except Exception as e:
        print(f"❌ Failed to send to {email}: {e}")