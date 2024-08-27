from slixmpp import ClientXMPP
from tkinter import messagebox
from Frontend.home import HomeWindow
import asyncio
from asyncio.exceptions import CancelledError

class EchoBot(ClientXMPP):

    """
    A simple Slixmpp bot that will echo messages it
    receives, along with a short thank you message.
    """

    def __init__(self, jid, password, login_window):
        ClientXMPP.__init__(self, jid, password)
        self.login_window = login_window
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
        self.login_window.destroy()
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
        If the authentication attempt fails, an error message is displayed.
        And the client is disconnected from the server.
        """
        messagebox.showerror("Error", "Failed to authenticate with the server credentials")
        print("ERROR: Authentication Failed")
        print("INFO: Client disconnected from the server")
        self.disconnect()
        

    async def init_home_gui(self):
        """
        Initialize the home GUI for the user.
        """
        home_window = HomeWindow(self)
        home_window.root.mainloop()
        await asyncio.sleep(0.01)
