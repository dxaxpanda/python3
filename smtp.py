
from email.mime.text import MIMEText
import smtplib

class Colour:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

local_mail = 'root@localhost'
dest_mail = 'jeremy.mirre@skores.com'
message = MIMEText("Disk space is getting low.")


#message["Subject"] = Colour.RED + \
#                    "WARNING: LOW DISK SPACE " + \
#                     Colour.END

message["Subject"] = "WARNING: LOW DISK SPACE"
message["From"] = local_mail
message["TO"] = dest_mail


server = smtplib.SMTP("smtp.gmail.com", 587)






server.starttls()
server.ehlo()

connection_status = False #
while connection_status is False:
    try:
        print("Attempting connection...")
        server.login("jeremy.mirre@skores.com", input("Please provide your password > "))
        connection_status = True # connected
        print("Sending message following message :", message.as_string())
        server.sendmail(local_mail, dest_mail, message.as_string()) # send message

        # close connection
        server.quit()
    except smtplib.SMTPAuthenticationError as e:
        print("Wrong password. Try again.")
        pass
