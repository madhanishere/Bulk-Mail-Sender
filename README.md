# BulkMail — General-Purpose Bulk Email Sender

**BulkMail** is a Python-based application for sending personalized bulk emails to multiple recipients via Gmail’s SMTP service. It supports flexible use cases such as sending reports, invitations, newsletters, announcements, and more — with customizable message content and recipient data fields.

## Features
- Sends personalized emails using data from a CSV file
- Supports dynamic fields and message customization
- Secure connection via Gmail SMTP (SSL)
- Works for any type of recipient communication
- No third-party libraries required
- Easily extensible to handle attachments or HTML content



<h2>Project Structure</h2>
<pre>
bulkmail
├── send_emails.py       # Main Python script to send emails
├── recipients.csv       # CSV file containing recipient data
|                            The structure of this file is flexible.
|                            You define the columns based on your use case.
|                            For example:
|                             - For reports: email,name,report_type
|                             - For invites: email,name,event_name,event_date
|                             - For general use: email,name,message 
└── README.md            # Project documentation 
</pre>



## CSV File Format
The structure of the CSV file is **flexible** and depends on the use case. You can define and use any number of columns to suit your specific message structure.

For example:
### For Annual Reports:


## Security Recommendations
- Use Gmail App Passwords for authentication (especially if 2FA is enabled)
- Avoid hardcoding credentials
- Do not commit sensitive files to public repositories

## Customization Options
- Add support for file attachments (e.g., PDF reports)
- Use HTML content for visually rich emails
- Implement logging for status tracking
- Add email scheduling or sending delay logic

## Example Use Cases
- Sending annual or financial reports
- Event invitations for shareholders
- Policy or regulatory announcements
- Company newsletters or updates
- Personalized notifications to clients





