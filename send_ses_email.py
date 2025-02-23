import boto3
from botocore.exceptions import ClientError

# Set up AWS SES client
ses_client = boto3.client("ses", region_name="us-east-1")  # Change to your region


def send_email(sender, recipient, subject, body_text, body_html):
    try:
        # Send email using SES
        response = ses_client.send_email(
            Source=sender,
            Destination={"ToAddresses": [recipient]},
            Message={
                "Subject": {"Data": subject},
                "Body": {"Text": {"Data": body_text}},
            },
        )

        print(f"Email sent! Message ID: {response['MessageId']}")

    except ClientError as e:
        print(f"Error sending email: {e.response['Error']['Message']}")


"""
# Example usage
sender = "abc@prabodhagarwal.com"  # Verified email in SES
recipient = "agrawalpriyanka1612@gmail.com"  # Recipient's email
subject = "Test Email from SES"
body_text = "This is a test email sent from SES using boto3."
body_html = (
    "<html><body><h1>This is a test email sent from SES using boto3.</h1></body></html>"
)

send_email(sender, recipient, subject, body_text, body_html)
"""
