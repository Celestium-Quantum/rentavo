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
        print(f"Reminder sent to {to_email
