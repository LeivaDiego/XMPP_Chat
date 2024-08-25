from slixmpp import ClientXMPP
from slixmpp.exceptions import IqError, IqTimeout, XMPPError

class XMPPClient(ClientXMPP):
    """
    XMPP client class that extends the ClientXMPP class from slixmpp.
    This class is used to create an XMPP client that can connect to an XMPP server.

    Attributes:
        jid -- The JID (Jabber ID) of the user
        password -- The password of the user
        register -- Boolean flag to indicate if the user should be registered

    Methods:
        connect_and_run -- Method to connect to the XMPP server and run the client
        start -- Method to handle the session start event
        register_account -- Method to handle the registration of a new account
        message -- Method to handle incoming messages
    """
    def __init__(self, jid, password, register=False):
        # Initialize the XMPP client
        super().__init__(jid, password)
        self.register = register
    
        # Event handlers for the XMPP client
        self.add_event_handler("session_start", self.start)

        # Register event handler for registration if register flag is set
        if self.register:
            self.add_event_handler("register", self.handle_registration)
    
        self.add_event_handler("message", self.message)

    async def start(self, event):
        # Start the XMPP client session
        self.send_presence()
        try:
            await self.get_roster()
            print(f"Logged in as {self.boundjid.bare}")
        except IqError as e:
            print("An error occurred while getting the roster: %s" % 
                    e.iq['error']['condition'])
            self.disconnect()
        except IqTimeout:
            print("No response from server.")
            self.disconnect()
        except XMPPError as e:
            print("An error occurred: %s" % e)
            self.disconnect()
        

    async def handle_registration(self, iq):
        # Handle the registration process for a new account
        resp = self.Iq()
        resp['type'] = 'set'
        resp['register']['username'] = self.boundjid.user
        resp['register']['password'] = self.password
        try:
            await resp.send()
            print("Account created for %s!" % self.boundjid)
        except IqError as e:
            print("Could not register account: %s" %
                    e.iq['error']['text'])
            self.disconnect()
        except IqTimeout:
            print("No response from server.")
            self.disconnect()
        except XMPPError as e:
            print("An error occurred: %s" % e)
            self.disconnect()

    def message(self, msg):
        # Echo bot logic
        if msg['type'] in ('chat', 'normal'):
            # Extract the sender's username from the JID
            sender = str(msg['from']).split('/')[0]
            print(f"Received message from {sender}: \t{msg['body']}")
            # Send an echo message back to the sender
            msg.reply(f"Echo: {msg['body']}").send()


    def connect_and_run(self):
        # Connect to the XMPP server and run the client
        self.register_plugin('xep_0030') # Service Discovery
        self.register_plugin('xep_0004') # Data forms
        self.register_plugin('xep_0066') # Out-of-band Data
        self.register_plugin('xep_0077') # In-band Registration
        self.connect(disable_starttls=True, use_ssl=False)
        self.process(forever=False) 
