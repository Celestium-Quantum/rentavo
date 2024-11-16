import unittest
from unittest.mock import patch, mock_open, MagicMock
import pandas as pd
from sample import load_data, send_email, send_rental_reminders

class TestRentalReminder(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="dummy data")
    @patch("pandas.read_excel")
    def test_load_data_success(self, mock_read_excel, mock_open_file):
        # Setup mock for pandas.read_excel
        mock_read_excel.return_value = pd.DataFrame({
            "Name": ["John Doe"],
            "Email": ["john@example.com"],
            "Due Amount": [500],
            "Due Date": ["2024-11-30"]
        })

        # Call the function
        result = load_data("tenants.xlsx")
        
        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(result.iloc[0]["Name"], "John Doe")
        self.assertEqual(result.iloc[0]["Email"], "john@example.com")
        self.assertEqual(result.iloc[0]["Due Amount"], 500)

    @patch("smtplib.SMTP")
    def test_send_email_success(self, mock_smtp):
        # Mock SMTP server
        mock_server = MagicMock()
        mock_smtp.return_value = mock_server

        # Call the function
        send_email("recipient@example.com", "Test Subject", "Test Body")

        # Assertions
        mock_server.starttls.assert_called_once()
        mock_server.login.assert_called_once()
        mock_server.sendmail.assert_called_once()
        mock_server.quit.assert_not_called()  # Because we use a context manager

    @patch("sample.load_data")
    @patch("sample.send_email")
    def test_send_rental_reminders(self, mock_send_email, mock_load_data):
        # Mock load_data return value
        mock_load_data.return_value = pd.DataFrame({
            "Name": ["Alice Smith"],
            "Email": ["alice@example.com"],
            "Due Amount": [800],
            "Due Date": ["2024-11-30"]
        })

        # Call the function
        send_rental_reminders("tenants.xlsx")

        # Assertions
        mock_load_data.assert_called_once_with("tenants.xlsx")
        mock_send_email.assert_called_once_with(
            "alice@example.com",
            "Rental Payment Reminder for Alice Smith",
            "Dear Alice Smith,\n\n"
            "This is a friendly reminder that your rental payment of $800 "
            "is due on 2024-11-30. Please ensure the payment is completed by then.\n\n"
            "Best regards,\nYour Property Management Team"
        )

if __name__ == "__main__":
    unittest.main()
