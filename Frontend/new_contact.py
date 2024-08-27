import tkinter as tk
from tkinter import messagebox

class AddContactWindow:
    """
    The AddContactWindow class is used to create a window for adding a new contact to the roster.
    The window allows the user to enter a username and add it to their roster.
    """

    def __init__(self, xmpp_client):
        self.client = xmpp_client
        self.root = tk.Toplevel()  # Use Toplevel to create a new window
        self.root.title("Add New Contact")
        self.root.resizable(False, False)
        self.center_window(400, 150)

        self.initialize_items()

    def initialize_items(self):
        """
        Initialize the UI elements of the window.
        """
        # Create a label and entry for the username
        tk.Label(self.root, text="Enter Username (e.g., user@alumchat.lol):").pack(pady=10)
        self.username_entry = tk.Entry(self.root, width=40)
        self.username_entry.pack(pady=5)

        # Create an "Add Contact" button
        tk.Button(self.root, text="Add Contact", command=self.add_contact).pack(pady=20)

    def add_contact(self):
        """
        Add the contact to the roster after validating the username.
        """
        username = self.username_entry.get().strip()

        # Validate that the username ends with '@alumchat.lol'
        if not username.endswith("@alumchat.lol"):
            messagebox.showerror("Invalid Username", "Username must end with '@alumchat.lol'")
            return

        # Send the subscription request to add the contact
        try:
            self.client.send_presence_subscription(username)
            messagebox.showinfo("Success", f"Successfully added {username} to your contacts.")
            self.root.destroy()  # Close the window on success
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add the contact: {str(e)}")

    def center_window(self, width, height):
        """
        Center the window on the screen based on the width and height provided.
        """
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')