# TODO: Create dependencies.txt
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Load tenant data from Excel
def load_data(file_path):
    df = pd.read_excel(file_path)
    return df

# Function to send an email
def send_email(to_email, subject, body):
    # Define SMTP server credentials
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_user = 'your_email@example.com'
    smtp_password = 'your_password'
    
    # Create email message
    message = MIMEMultipart()
    message['From'] = smtp_user
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    
    # Connect to SMTP server and send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to_email, message.as_string())
    
    print(f"Reminder sent to {to_email}")

# Function to process data and send reminders
def send_rental_reminders(file_path):
    data = load_data(file_path)
    
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

# Schedule the task
file_path = 'tenants.xlsx'

def schedule_reminders():
    # Schedule the task to run monthly on a specific day
    schedule.every().month.at("09:00").do(send_rental_reminders, file_path)

    while True:
        schedule.run_pending()
        time.sleep(1)

# Call the scheduling function to start the system
if __name__ == "__main__":
    schedule_reminders()
