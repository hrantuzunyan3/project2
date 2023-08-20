import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# Configure your Gmail account credentials
sender_email = 'hrant1998@gmail.com'
sender_password = 'uluaoylxwgebeaot'

# Recipient's email address
recipient_email = "hrant1998@gmail.com"

# Check interval in seconds
check_interval = 300  # 5 minutes

# Initialize the set to store observed IP addresses
observed_ips = set()

def send_email(new_ip):
    subject = "New IP Address Detected"
    message = f"New IP address detected: {new_ip}"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    # Connect to Gmail's SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

while True:
    try:
        # Get the current IP table rules using subprocess
        iptables_output = subprocess.check_output(["iptables", "-L", "-n"])
        iptables_lines = iptables_output.decode("utf-8").splitlines()

        # Extract IP addresses from the output
        current_ips = set()
        for line in iptables_lines:
            parts = line.split()
            if len(parts) >= 4 and parts[0] == "ACCEPT" and parts[3] != "0.0.0.0/0":
                current_ips.add(parts[3])

        # Find new IP addresses
        new_ips = list(current_ips - observed_ips)

        # Send email if new IPs are found
        if new_ips:
            for new_ip in new_ips:
                send_email(new_ip)
                observed_ips.add(new_ip)
                print(f"New IP address detected: {new_ip}")

        time.sleep(check_interval)

    except KeyboardInterrupt:
        print("Script terminated by user.")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
