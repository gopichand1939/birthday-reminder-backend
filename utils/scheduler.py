import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datetime import datetime
from models.db import collection
from utils.email_sender import send_birthday_email

def check_and_send_birthday_emails():
    now = datetime.now().strftime('%Y-%m-%d %H:%M')  # Current time (match format exactly)

    birthdays = list(collection.find())
    for person in birthdays:
        send_at = person.get("sendAt")  # Expected format: 2025-05-17T12:08

        if send_at:
            try:
                # Convert sendAt to matching datetime format for comparison
                scheduled_time = datetime.strptime(send_at, "%Y-%m-%dT%H:%M").strftime('%Y-%m-%d %H:%M')

                # Check match + not already sent
                if scheduled_time == now and not person.get("emailSent", False):
                    send_birthday_email(person["name"], person["email"])

                    # Mark as sent in DB
                    collection.update_one(
                        {"_id": person["_id"]},
                        {"$set": {"emailSent": True}}
                    )
                    print(f"✅ Sent to {person['email']} at {scheduled_time}")
            except Exception as e:
                print(f"❌ Error processing entry for {person.get('name')}: {e}")

if __name__ == "__main__":
    check_and_send_birthday_emails()
