import boto3
from datetime import datetime

# Initialize the SES client
ses = boto3.client('ses', region_name='us-east-1')

# Sender and receiver emails (both must be verified in SES if in sandbox)
sender_email = "pavankumarrs099@gmail.com"
recipient_email = "psrinivasulu@scu.edu"

# Current datetime
now = datetime.now()

# Email subject and body
subject = 'Santa Clara University | Your attendance report as on {}'.format(now)
body_text = (
    "Hello!\n\n"
    "This is to let you know that your attendance is 86% as on {}.\n\n"
    "Thanks,\nSanta Clara University".format(now.strftime('%Y-%m-%d'))
)

# Send the email
response = ses.send_email(
    Source=sender_email,
    Destination={
        'ToAddresses': [
            recipient_email,
        ],
    },
    Message={
        'Subject': {
            'Data': subject,
        },
        'Body': {
            'Text': {
                'Data': body_text,
            },
        }
    }
)


print("Email sent to {0}!! Message ID:{1}".format(recipient_email, response['MessageId']))

