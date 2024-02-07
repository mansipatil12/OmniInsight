import imaplib
import email
from email.header import decode_header

def fetch_emails(username, password, server="imap.example.com", folder="INBOX", criteria="(UNSEEN)"):
    """
    Fetch unseen emails from an IMAP server.
    
    Args:
    username (str): The email username.
    password (str): The email password.
    server (str): The IMAP server hostname (default is "imap.example.com").
    folder (str): The email folder to fetch emails from (default is "INBOX").
    criteria (str): The search criteria for fetching emails (default is "(UNSEEN)").
    
    Returns:
    list: A list of email message objects.
    """
    # Connect to the IMAP server
    mail = imaplib.IMAP4_SSL(server)
    mail.login(username, password)
    mail.select(folder)
    
    # Search for unseen emails based on criteria
    result, data = mail.search(None, criteria)
    
    # Fetch emails
    emails = []
    for num in data[0].split():
        result, email_data = mail.fetch(num, '(RFC822)')
        raw_email = email_data[0][1]
        msg = email.message_from_bytes(raw_email)
        emails.append(msg)
    
    # Close the connection
    mail.close()
    mail.logout()
    
    return emails

def extract_email_content(email_msg):
    """
    Extract content from an email message.
    
    Args:
    email_msg (email.message.Message): The email message object.
    
    Returns:
    str: The email content as a string.
    """
    content = ""
    for part in email_msg.walk():
        if part.get_content_type() == "text/plain":
            content += part.get_payload(decode=True).decode(part.get_content_charset(), 'ignore')
    return content

# Example usage
if __name__ == "__main__":
    # Example email credentials and server details
    username = "your_email@example.com"
    password = "your_password"
    server = "imap.example.com"
    folder = "INBOX"
    criteria = "(UNSEEN)"  # Fetch only unseen emails
    
    # Fetch unseen emails
    emails = fetch_emails(username, password, server, folder, criteria)
    
    # Extract content from emails
    for email_msg in emails:
        content = extract_email_content(email_msg)
        print("Subject:", email_msg['Subject'])
        print("From:", email_msg['From'])
        print("Content:", content)
        print("\n")
