import tkinter as tk
from tkinter import ttk

class UpdatePresenceWindow:
    """
    The UpdatePresenceWindow class is used to create a window for updating the user's presence.
    The window allows the user to select a presence option from a dropdown menu.
    The user can also enter a custom presence message.

    The window provides an "Update Presence" button to update the user's presence based on the selected option.

    Attributes:
        client: The XMPP client instance used to update the presence.
        root: The Tkinter Toplevel window.
        presence_options: A list of predefined presence options.
        presence_var: The Tkinter StringVar for the selected presence option.
        presence_selector: The Tkinter Combobox for selecting the presence option.
        custom_message_entry: The Tkinter Entry for entering a custom presence message.

    Methods:
        initialize_items: Initialize the UI elements of the window.
        update_presence: Update the presence based on the selected presence option.
        center_window: Center the window on the screen based on the width and height provided.
    """
    def __init__(self, xmpp_client, parent):
        # Initialize the window
        self.client = xmpp_client
        self.parent = parent
        self.root = tk.Toplevel()  # Use Toplevel to create a new window
        self.root.title("Update Presence")
        self.root.resizable(False, False)
        self.center_window(400, 200)
        
        # Predefined presence options
        self.presence_options = ["Available", "Away", "Do Not Disturb", "Extended Away"]

        # Initialize the UI elements
        self.initialize_items()


    def initialize_items(self):
        """
        Initialize the UI elements of the window.
        """
        # Create a dropdown menu for selecting presence
        tk.Label(self.root, text="Select Presence:").pack(pady=10)
        self.presence_var = tk.StringVar(value=self.presence_options[0])
        self.presence_selector = ttk.Combobox(self.root, textvariable=self.presence_var, values=self.presence_options, state="readonly")
        self.presence_selector.pack(pady=5)

        # Create a text box for presence message (always enabled)
        tk.Label(self.root, text="Status Message:").pack(pady=10)
        self.custom_message_entry = tk.Entry(self.root, state=tk.NORMAL)
        self.custom_message_entry.pack(pady=5, fill=tk.X, padx=20)

        # Create an update button
        tk.Button(self.root, text="Update Presence", command=self.update_presence).pack(pady=20)

    def update_presence(self):
        """
        Update the presence based on the selected presence option and status message.
        If no status message is provided, it will be set to "None".

        This method will call the client's update_presence method to update the presence.
        """
        # Get the selected presence
        presence = self.presence_var.get()

        # Get the custom message from the entry field
        custom_message = self.custom_message_entry.get() if self.custom_message_entry.get().strip() else "None"

        # Call the client's method to update the presence
        self.client.update_presence(presence, custom_message)
        self.parent.update_user_info()

        # Close the window
        self.root.destroy()


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
