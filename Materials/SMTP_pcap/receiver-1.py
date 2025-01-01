import smtplib

server = smtplib.SMTP('localhost', 1025)
server.set_debuglevel(1)

from_addr = "sender@example.com"
to_addr = "receiver@example.com"
msg = """\
From: sender@example.com
To: receiver@example.com
Subject: CTF-Network

Thanks for your time. My name is Mr. Drever.
I would like to create a problem in CTF-Network, but I don't know what kind of problem would be good,
I would like to know what kind of problems would be good.

Thank you very much in advance.


"""

server.sendmail(from_addr, to_addr, msg)
server.quit()
