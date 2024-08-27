from slixmpp import ClientXMPP
from tkinter import messagebox
from Frontend.home import HomeWindow
import asyncio
from slixmpp.exceptions import IqError, IqTimeout

class XMPP_Client(ClientXMPP):

    """
    A simple Slixmpp bot that will echo messages it
    receives, along with a short thank you message.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Singleton pattern to ensure only one instance of the XMPP_Client is created.
        """
        if cls._instance is None:
            cls._instance = super(XMPP_Client, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, jid, password, window=None, register=False):
        if not hasattr(self, 'initialized'):
            super().__init__(jid, password)
            self.window = window
            self.registration = register
            self.initialized = True

            # Register event handlers
            if self.registration:
                self.add_event_handler("register", self.register)

            # Set event Handlers
            self.add_event_handler("session_start", self.start)
            self.add_event_handler("message", self.message)
            self.add_event_handler("failed_auth", self.failed_auth)
            print("SUCCES: ClientXMPP initialized")


    async def start(self, event):
        """
        Process the session_start event.

        Typical actions for the session_start event are
        requesting the roster and broadcasting an initial
        presence stanza.

        Arguments:
            event -- An empty dictionary. The session_start
                     event does not provide any additional
                     data.
        """
        self.send_presence()
        await self.get_roster()
        print("SUCCESS: user connected to the server")
        messagebox.showinfo("Success", "Successfully authenticated with the server")
        self.window.root.destroy()
        await self.init_home_gui()

    def message(self, msg):
        """
        Process incoming message stanzas. Be aware that this also
        includes MUC messages and error messages. It is usually
        a good idea to check the messages's type before processing
        or sending replies.

        Arguments:
            msg -- The received message stanza. See the documentation
                   for stanza objects and the Message stanza to see
                   how it may be used.
        """
        if msg['type'] in ('chat', 'normal'):
            msg.reply("Thanks for sending\n%(body)s" % msg).send()

    def failed_auth(self, event):
        """
        Handler for failed authentication attempts.
        If the authentication attempt fails, an error message is displayed,
        and the client is disconnected from the server.
        """
        def handle_failed_auth():
            """
            Internal function to handle failed authentication.
            """
            # Display an error message and update the login window
            messagebox.showerror("Error", "Failed to authenticate with the server credentials")
            self.window.show_authentication_failed()
           
            # Add a print statement to show the error message in the console
            print("ERROR: Authentication Failed")
            print("INFO: Client disconnected from the server")
            
            # Disconnect the client from the server
            self.disconnect()

        # Use after to schedule the error message and disconnection
        self.window.root.after(0, handle_failed_auth)


    async def register(self, iq):
        """
        Fill out and submit a registration form.
        Will be called if the registration flag is set to True. 
        This method will create a new account for the user.
        """
        # Create a new Iq object and set the type to 'set'
        resp = self.Iq()
        resp['type'] = 'set'
        resp['register']['username'] = self.boundjid.user
        resp['register']['password'] = self.password

        # Send the Iq object to the server and handle the response
        try:
            await resp.send()
            messagebox.showinfo("Success", "Account created for %s!" % self.boundjid)
            print("SUCCESS: Account created for %s!" % self.boundjid)
        except IqError as e:
            messagebox.showerror("Error", "Could not register account: %s" % e.iq['error']['text'])
            print("ERROR: Could not register account: %s" %
                    e.iq['error']['text'])
            self.window.show_registration_failed()
            self.disconnect()
        except IqTimeout:
            messagebox.showerror("Error", "No response from server.")
            print("TIMEOUT: No response from server.")
            self.window.show_registration_failed()
            self.disconnect()


    async def init_home_gui(self):
        """
        Initialize the home GUI for the user.
        """
        home_window = HomeWindow(self)
        home_window.root.mainloop()
        await asyncio.sleep(0.01)

    def logout(self):
        self.disconnect()
        print("INFO: Client disconnected from the server")
        XMPP_Client._instance = None
        self.initialized = False
        print("INFO: XMPP Client instance cleaned and reset")
