import tkinter as tk
from tkinter import ttk

class HomeWindow:
    """
    The HomeWindow class is used to create a home window for the application.
    The home window is displayed after the user has successfully logged in.
    """
    def __init__(self, xmpp_client):
        self.root = tk.Tk()
        self.root.title("XMPP Chat Home")
        self.client = xmpp_client
        self.root.resizable(False, False)
        self.configure_layout()
        self.center_window(900, 600)

        # Handle the window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Display the current user's JID and presence
        self.update_user_info()

        # Fetch and display contacts
        self.update_contacts_list()

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
        tk.Button(menu_frame, text="Logout", command=self.logout).pack(fill=tk.X, pady=5)
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
        self.contact_selector.bind("<<ComboboxSelected>>", self.display_contact_info)

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
    

    def update_user_info(self):
        """
        Update the user information displayed in the HomeWindow.
        """
        try:
            user_jid = self.client.boundjid.bare
            status = "Online"  # Default value, update as needed based on actual presence
            self.user_info_label.config(text=f"User: {user_jid}\nStatus: {status}")
            print(f"SUCCESS: User information retrieved: {user_jid}, {status}")
        except Exception as e:
            print(f"ERROR: Failed to update user information: {e}")


    def update_contacts_list(self):
        """
        Fetch the contacts from the XMPP server and update the dropdown menu.
        Exclude the user's own JID from the contact list.
        """
        try:
            roster = self.client.client_roster
            own_jid = str(self.client.boundjid.bare)  # Get the user's own JID without the resource part
            contacts = [jid for jid in roster.keys() if jid != own_jid]
            self.contact_selector['values'] = contacts
            print(f"SUCCESS: Contacts retrieved and populated, excluding own JID: {own_jid}")
        except Exception as e:
            print(f"ERROR: Failed to retrieve contacts: {e}")



    def display_contact_info(self, event):
        """
        Display the selected contact's information in the contact info text box.
        """
        # Get the selected contact from the dropdown menu
        selected_contact = self.contact_selector.get()

        # Display the contact information in the text box
        if selected_contact:
            # Get the presence information for the selected contact
            roster = self.client.client_roster

            if selected_contact in roster:
                # Default values
                presence_value = "Offline"
                status = "None"

                # Check and iterate through presence information
                for _, presence in roster.presence(selected_contact).items():
                    presence_value = presence['show'] or 'Offline'
                    status = presence['status'] or 'None'
                    # Only check the first presence value
                    break  

                contact_info_text = f"JID: {selected_contact}\nPresence: {presence_value}\nStatus: {status}"
                self.contact_info.config(state=tk.NORMAL)
                self.contact_info.delete(1.0, tk.END)
                self.contact_info.insert(tk.END, contact_info_text)
                self.contact_info.config(state=tk.DISABLED)
            else:
                self.contact_info.config(state=tk.NORMAL)
                self.contact_info.delete(1.0, tk.END)
                self.contact_info.insert(tk.END, "No information available")
                self.contact_info.config(state=tk.DISABLED)


    
    def logout(self):
        """
        Logout the user and disconnect the client from the server.
        """
        self.client.disconnect()
        print("INFO: Client disconnected from the server")
        self.root.destroy()
        print("INFO: Please wait while tasks are being cleaned up")
        from Frontend.welcome import WelcomeWindow
        welcome_window = WelcomeWindow()
        welcome_window.root.mainloop()

    def on_close(self):
        """
        Handle the window close event.
        """
        self.client.disconnect()
        print("INFO: Client disconnected from the server")
        self.root.destroy()
        print("INFO: Please wait while tasks are being cleaned up")

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
