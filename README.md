# rental-reminder
Outline for a rental payment reminder system that reads tenant details and rental amounts from an Excel spreadsheet, then sends out automated reminders

### Architecture

1. Data Input: A Microsoft Excel spreadsheet contains tenants’ details, including names, email addresses, and payment amounts.

2. Data Processing: The system reads and processes data from the Excel sheet using Python’s pandas library.

3. Notification Service: After processing, the system formats and sends reminders using an email API (e.g., SMTP or a service like SendGrid or Amazon SES).

4. Scheduler: Uses a task scheduler (like cron for Unix or schedule in Python) to send reminders on a set date every month.

### Architecture diagram (base)

![image](https://github.com/user-attachments/assets/4347f95a-9771-40a5-a370-f727d3bf945d)

### AWS base architecture

![image](https://github.com/user-attachments/assets/7dc9c7dd-3a13-4fcd-bc88-2ef369c06b09)

### Sequence diagram (base)

![seqrental](https://github.com/user-attachments/assets/38b8637c-3598-413f-8596-1bf2826571e5)

### Placeholder system design

![image](https://github.com/user-attachments/assets/06dc1af8-edb7-4996-939b-293fd8812380)

#### v2

![image](https://github.com/user-attachments/assets/85240d66-af9d-4802-bb14-1550a87b7763)

### Components and workflow

1. Excel File: Contains tenant information and monthly rent. Columns may include:

- Name
- Email
- Due Amount
- Due Date
- Python Data Handler: Reads and processes data using pandas.

2. Email Notification Service: Configured to send personalized email reminders.

3. Scheduler: Triggers the reminder system on a set date every month.

##### Scheduler Setup (Alternative)

For more flexibility, to consider setting up a cron job or task scheduler that calls this script at regular intervals if deploying in a Linux or Unix environment.

This approach provides a robust, scalable system for automating rental payment reminders.


