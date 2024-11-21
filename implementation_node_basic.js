# base nodejs implementation
const fs = require('fs');

// Mock loading data from a file (JSON format for simplicity)
function loadData(filePath) {
    if (!fs.existsSync(filePath)) {
        throw new Error("File not found");
    }
    const data = fs.readFileSync(filePath, 'utf8');
    return JSON.parse(data);
}

// Mock sending an email
function sendEmail(recipient, subject, body) {
    console.log(`Email sent to ${recipient}`);
    console.log(`Subject: ${subject}`);
    console.log(`Body: ${body}`);
    return true;
}

// Function to send rental reminders
function sendRentalReminders(filePath) {
    const tenants = loadData(filePath);
    tenants.forEach((tenant) => {
        const { Name, Email, "Due Amount": dueAmount, "Due Date": dueDate } = tenant;
        const subject = `Rental Payment Reminder for ${Name}`;
        const body = `Dear ${Name},\n\nThis is a friendly reminder that your rental payment of $${dueAmount} is due on ${dueDate}. Please ensure the payment is completed by then.\n\nBest regards,\nYour Property Management Team`;
        sendEmail(Email, subject, body);
    });
}

module.exports = { loadData, sendEmail, sendRentalReminders };
