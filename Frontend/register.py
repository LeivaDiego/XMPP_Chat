import tkinter as tk
from tkinter import messagebox
from Backend.client import XMPP_Client

class RegisterForm:
    """
    The RegisterForm class is used to create a registration form for the application.
    The form contains three input fields for the username, password, and confirm password.

    Attributes:
        - root: The main window of the registration form
        - username_entry: The entry field for the username
        - password_entry: The entry field for the password
        - confirm_password_entry: The entry field for confirming the password

    Methods:
        - initialize_items: Initializes the items on the registration form (labels, entry fields, buttons)
        - submit_form: Validates the input fields and creates a new account
        - return_to_welcome: Closes the registration form and returns to the welcome window
        - center_window: Centers the window on the screen
    """

    def __init__(self):
        # Create the main window of the registration form
        self.root = tk.Tk()
        self.root.title("Sign Up Form")
        self.root.resizable(False, False)
        self.username_entry = None
        self.password_entry = None
        self.loading_label = None
        self.confirm_password_entry = None
        self.initialize_items()
        self.center_window(400, 200)

    def initialize_items(self):
        """
        Initialize the items on the registration form:
            - Labels
            - Entry fields
            - Buttons
        The labels are used to display text on the form.
        The entry fields are used to input the username, password, and confirm password.
        The buttons are used to interact with the form (register, return).
        """
        # Create a frame to hold the form items
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Create a label for the username field
        username_label = tk.Label(form_frame, text="Username:")
        username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = tk.Entry(form_frame, width=30)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        # Create a label for the password field
        password_label = tk.Label(form_frame, text="Password:")
        password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = tk.Entry(form_frame, width=30)
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Create a label for the confirm password field
        confirm_password_label = tk.Label(form_frame, text="Confirm Password:")
        confirm_password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.confirm_password_entry = tk.Entry(form_frame, show="*", width=30)
        self.confirm_password_entry.grid(row=2, column=1, padx=10, pady=5)

        # Create a frame to hold the buttons
        button_frame = tk.Frame(form_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)

        # Create a return button that calls the return_to_welcome method
        return_button = tk.Button(button_frame, text="Return", command=self.return_to_welcome)
        return_button.grid(row=0, column=1, padx=10)

        # Create a register button that calls the submit_form method
        signup_button = tk.Button(button_frame, text="Register", command=self.submit_form)
        signup_button.grid(row=0, column=2, padx=10)

        # Add a loading label but keep it hidden initially
        self.loading_label = tk.Label(self.root, text="Registering...", font=("Arial", 10))
        self.loading_label.pack(pady=10)
        self.loading_label.pack_forget()


    def submit_form(self):
        """
        Validate the input fields and create a new account.

        The username must end with '@alumchat.lol'.
        The password and confirm password must match.

        If the input is valid, display a success message and close the registration form.
        If the input is invalid, display an error message.
        """
        # Get the values from the input fields
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Validate that username ends with '@alumchat.lol'
        if not username.endswith("@alumchat.lol"):
            messagebox.showerror("Invalid Username", "Username must end with '@alumchat.lol'")
            return

        # Validate that all fields are filled
        if not username or not password or not confirm_password:
            messagebox.showwarning("Input Error", "Please fill in all fields")
            return

        # Validate that password and confirm password match
        if password != confirm_password:
            messagebox.showerror("Password Mismatch", "Passwords do not match")
            return

        # Create an isntance of the Client class
        xmpp = XMPP_Client(username, password, window=self, register=True)
        
        # Show the loading label
        self.loading_label.config(text="Registering...", fg="black")
        self.loading_label.pack()
        self.loading_label.update_idletasks()

        # Register the user with the server
        # and connect to the server
        xmpp.connect(disable_starttls=True, use_ssl=False)

        # Register the xep_0077 plugin
        xmpp.register_plugin('xep_0077')

        # Register the user with the server    
        xmpp.process(forever=False, timeout=10)


    def return_to_welcome(self):
        """
        Close the registration form and return to the welcome window.
        """
        self.root.destroy()                         # Close the registration form
        from Frontend.welcome import WelcomeWindow  # Import the WelcomeWindow class
        welcome_window = WelcomeWindow()            # Create an instance of the WelcomeWindow class
        welcome_window.root.mainloop()              # Open the welcome window


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

    def show_registration_failed(self):
        """
        Update the loading label to show a registration failure message.
        """
        self.loading_label.config(text="Registration Failed... Try again", fg="red")
        self.loading_label.update_idletasks()