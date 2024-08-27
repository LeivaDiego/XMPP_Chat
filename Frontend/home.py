import tkinter as tk
from tkinter import ttk

class HomeWindow:
    """
    The HomeWindow class is used to create a home window for the application.
    The home window is displayed after the user has successfully logged in.
    """
    # TODO: Implement logic for the HomeWindow class
    # Currently, the HomeWindow class is the template that will be used on final implementation.
    def __init__(self, xmpp_client):
        self.root = tk.Tk()
        self.root.title("XMPP Chat Home")
        self.client = xmpp_client
        self.root.resizable(False, False)
        self.configure_layout()

        # Handle the window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def configure_layout(self):
        # Create the left-side menu
        menu_frame = tk.Frame(self.root)
        menu_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Create buttons for the left-side menu
        tk.Button(menu_frame, text="Show Contacts").pack(fill=tk.X, pady=5)
        tk.Button(menu_frame, text="Add New Contact").pack(fill=tk.X, pady=5)
        tk.Button(menu_frame, text="Join Group").pack(fill=tk.X, pady=5)
        tk.Button(menu_frame, text="Create New Group").pack(fill=tk.X, pady=5)
        tk.Button(menu_frame, text="Update Presence").pack(fill=tk.X, pady=5)
        tk.Button(menu_frame, text="Logout").pack(fill=tk.X, pady=5)
        tk.Button(menu_frame, text="Delete My Account").pack(fill=tk.X, pady=5)

        # Create a label or text box for displaying the current user's information at the bottom left
        self.user_info_label = tk.Label(menu_frame, text="User: Not logged in", anchor="w")
        self.user_info_label.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

        # Create the main chat area
        chat_frame = tk.Frame(self.root)
        chat_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create a frame for the contact selection and info display
        contact_frame = tk.Frame(chat_frame)
        contact_frame.pack(anchor=tk.W, fill=tk.X, pady=5)

        # Create a dropdown menu (Combobox) for selecting contacts
        self.contact_selector = ttk.Combobox(contact_frame, values=[], state="readonly")
        self.contact_selector.pack(side=tk.LEFT, padx=5)
        self.contact_selector.set("Select a contact")

        # Create a text box to display contact information
        self.contact_info = tk.Text(contact_frame, height=4, state=tk.DISABLED, wrap=tk.WORD)
        self.contact_info.pack(side=tk.RIGHT, fill=tk.X, padx=5)

        # Create a frame for the chat display area
        chat_display_frame = tk.Frame(chat_frame)
        chat_display_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        # Create a text widget for displaying messages with a scrollbar
        self.message_box = tk.Text(chat_display_frame, state=tk.DISABLED, wrap=tk.WORD)
        self.message_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a scrollbar to the message box
        scrollbar = tk.Scrollbar(chat_display_frame, command=self.message_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.message_box['yscrollcommand'] = scrollbar.set

        # Create a frame for the message input area
        message_input_frame = tk.Frame(chat_frame)
        message_input_frame.pack(fill=tk.X, pady=5)

        # Create an entry widget for message input
        self.message_entry = tk.Entry(message_input_frame)
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Create a send button
        tk.Button(message_input_frame, text="Send").pack(side=tk.RIGHT, padx=5)

    def logout(self):
        """
        Logout the user and disconnect the client from the server.
        """
        self.client.disconnect()
        print("INFO: Client disconnected from the server")
        self.root.destroy()
        print("INFO: Please wait while tasks are being cleaned up")

    def on_close(self):
        """
        Handle the window close event.
        """
        self.logout()

    def center_window(self, width, height):
        """
        Center the window on the screen based on the width and height provided.
        Calculates the x and y coordinates to position the window in the center of the
        screen based on the screen width and height.
        """
        screen_width = self.root.winfo_screenwidth()        # Get the screen width
        screen_height = self.root.winfo_screenheight()      # Get the screen height

        # Calculate the x and y coordinates to center the window
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')



home = HomeWindow(None)
home.root.mainloop()