import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your email and app password (for Gmail, use an App Password)
email_user = ""
email_password = ""
subject = "ANNUAL MEET 2025 "
with open('emails.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        email_send = line[0]
        name = line[1]
        id_no = line[2]

# CONTENTS
        text = f"""XYZ LTD

 
Date: 30 th August 2024.

Dear {name}
Identification Number : {id_no}


Dear Shareholder,

XYZ Company’s 38th Annual General Meeting (AGM) will be held on Saturday, 21st September 2024 at 11:00 A.M. IST via Video Conferencing (VC)/Other Audio Visual Means (OAVM), without physical presence, as per applicable laws and circulars.
The Notice of AGM, Annual Report, Board’s Report, Auditor’s Report, and Financial Statements for the year ended March 31, 2024 are sent to your registered email and are also available at www.xyzcompany.com.
Joining the AGM:
Members may join the meeting using their CDSL e-voting login credentials. Instructions are given in the AGM Notice.
E-Voting:Remote e-voting is open from 18th September 2024, 9:00 A.M. to 20th September 2024, 5:00 P.M. Members as of 14th September 2024 may vote electronically. E-voting will also be available during the AGM.
For help, visit www.evotingindia.com or contact helpdesk.evoting@cdslindia.com / 1800 22 5533.

Regards,
Compliance Officer
XYZ Company
123 Business Street, Mumbai – 400001 | Tel: 022-12345678"""

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject
        msg.attach(MIMEText(text, "plain"))

        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(email_user, email_password)
            server.sendmail(email_user, email_send, msg.as_string())
            server.quit()
            print(f"Email sent to {email_send}")
        except Exception as e:
            print(f"Failed to send email to {email_send}: {e}")
