import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email(receiver_email,subject,body):
    # Email configuration
    smtp_server = "smtp.gmail.com"  # Gmail SMTP server
    smtp_port = 587  # For starttls
    sender_email = "christophereleazar4@gmail.com"  # Your email
    password = ""  # Your email password or App Password

    

    # Create a multipart email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attach the PDF file
    pdf_filename = "CV_ELEAZAR Christopher Otniel.pdf"  # Path to your PDF file
    with open(pdf_filename, "rb") as pdf_file:
        pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
        pdf_attachment.add_header('Content-Disposition', 'attachment', filename=pdf_filename)
        msg.attach(pdf_attachment)


    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(sender_email, password)  # Log in to your email account
            server.send_message(msg)  # Send the email
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")