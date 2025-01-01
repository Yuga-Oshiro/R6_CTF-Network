from aiosmtpd.controller import Controller

class CustomSMTPHandler:
    async def handle_DATA(self, server, session, envelope):
        print(f"Message from: {envelope.mail_from}")
        print(f"Message to: {envelope.rcpt_tos}")
        print(f"Message content:\n{envelope.content.decode('utf8', errors='replace')}")
        print('-' * 50)
        return '250 Message accepted for delivery'

if __name__ == "__main__":
    controller = Controller(CustomSMTPHandler(), hostname='localhost', port=1025)
    print("SMTP server is running on localhost:1025")
    controller.start()
    try:
        input("Press Enter to stop the server.\n")
    finally:
        controller.stop()
