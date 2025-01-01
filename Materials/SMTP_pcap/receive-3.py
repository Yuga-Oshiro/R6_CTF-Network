import smtplib

server = smtplib.SMTP('localhost', 1025)
server.set_debuglevel(1)

from_addr = "sender@example.com"
to_addr = "receiver@example.com"
msg = """\
From: sender@example.com
To: receiver@example.com
Subject: CTF-Network

Thank you!
It's a lot of work to make a CTF problem, but I'll do my best!

It sure would be nice to make the current email exchange into a problem! I will write Flag in my next email.
Thank you so much!


"""

server.sendmail(from_addr, to_addr, msg)
server.quit()
