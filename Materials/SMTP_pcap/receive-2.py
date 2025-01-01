import smtplib

server = smtplib.SMTP('localhost', 1025)
server.set_debuglevel(1)

from_addr = "sender@example.com"
to_addr = "receiver@example.com"
msg = """\
From: sender@example.com
To: receiver@example.com
Subject: CTF-Network

Sorry for the delay!
I know it's hard to make problems for CTF. But this is a good opportunity to make problems, and it will further deepen my understanding of CTF, so good luck!

Yes, for example, how about making this email exchange into a CTF problem?

How about a problem where you use wireshark to see the contents of the email and get the Flag?

"""

server.sendmail(from_addr, to_addr, msg)
server.quit()