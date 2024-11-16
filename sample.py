"""
Rental Payment Reminder Script.

This script automates the sending of rental payment reminders via email.
It reads tenant information from an Excel file and sends personalized emails.
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import pandas as pd
import schedule
import os


def load_data(file_path):
    """
    Load tenant data from an Excel file.

    Args:
        file_path (str): Path to the Excel file.

    Returns:
        DataFrame: Loaded data as a pandas DataFrame.
    """
    try:
        df = pd.read_excel(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None


def send_email(to_email, subject, body):
    """
    Send an email using SMTP.

    Args:
        to_email (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body of the email.
    """
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_user = os.getenv("SMTP_USER", "your_email@example.com")
    smtp_password = os.getenv("SMTP_PASSWORD", "your_password")

    try:
        message = MIMEMultipart()
        message['From'] = smtp_user
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, to_email, message.as_string())
        print(f"Reminder sent to {to_email}")
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")


def send_rental_reminders(file_path):
    """
    Process tenant data and send rental payment reminders.

    Args:
        file_path (str): Path to the Excel file.
    """
    data = load_data(file_path)
    if data is None:
        return

    for _, row in data.iterrows():
        name = row['Name']
        email = row['Email']
        due_amount = row['Due Amount']
        due_date = row['Due Date']

        subject = f"Rental Payment Reminder for {name}"
        body = (f"Dear {name},\n\n"
                f"This is a friendly reminder that your rental payment of ${due_amount} "
                f"is due on {due_date}. Please ensure the payment is completed by then.\n\n"
                "Best regards,\nYour Property Management Team")

        send_email(email, subject, body)


FILE_PATH = 'tenants.xlsx'


def schedule_reminders():
    """
    Schedule rental payment reminders to be sent monthly.
    """
    schedule.every().month.at("09:00").do(send_rental_reminders, FILE_PATH)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    schedule_reminders()
