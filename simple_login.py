import os
import time
import logging
from dotenv import load_dotenv
import slixmpp

class EchoClient(slixmpp.ClientXMPP):
    def __init__(self, jid, password, recipient, message):
        slixmpp.ClientXMPP.__init__(self, jid, password)
        self.recipient = recipient
        self.message = message

        # Event handlers
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.message_handler)

    async def start(self, event):
        self.send_presence()
        await self.get_roster()

        # Send a message to the eco bot
        self.send_message(mto=self.recipient,
                          mbody=self.message,
                          mtype='chat')

    def message_handler(self, msg):
        if msg['type'] in ('chat', 'normal'):
            print(f"Received message from {msg['from']}: {msg['body']}")
            self.disconnect()

if __name__ == '__main__':
    # Load the .env file
    load_dotenv()

    # Get the environment variables
    jid = os.getenv("JID")
    password = os.getenv("PASSWORD")
    recipient = os.getenv("ECHOBOT")
    message = "Hello, EchoBot!"  # Message to send

    # Setup logging
    logging.basicConfig(level=logging.DEBUG,  # Set logging level to DEBUG
                        format='%(levelname)-8s %(message)s')

    if jid is None or password is None:
        raise ValueError("JID and PASSWORD must be set in the .env file")

    # Setup the EchoClient
    xmpp = EchoClient(jid, password, recipient, message)
    xmpp.register_plugin('xep_0030')  # Service Discovery
    xmpp.register_plugin('xep_0199')  # XMPP Ping

    # Connect to the XMPP server and start processing XMPP stanzas
    xmpp.connect()
    xmpp.process(forever=False)