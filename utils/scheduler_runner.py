import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import schedule
import time
from utils.scheduler import check_and_send_birthday_emails

# Run check every 1 minute
schedule.every(1).minutes.do(check_and_send_birthday_emails)

print("🎯 Scheduler active... checking every minute.")

while True:
    schedule.run_pending()
    time.sleep(60)
