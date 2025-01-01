import smtplib

server = smtplib.SMTP('localhost', 1025)
server.set_debuglevel(1)

from_addr = "sender@example.com"
to_addr = "receiver@example.com"
msg = """\
From: sender@example.com
To: receiver@example.com
Subject: CTF-Network

Flag is below!
kitCTF{smtp_flag_is_here}

"""

server.sendmail(from_addr, to_addr, msg)
server.quit()
