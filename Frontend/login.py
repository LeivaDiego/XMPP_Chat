import tkinter as tk
from tkinter import messagebox
from Backend.client import XMPP_Client

class LoginForm:
    """
    The LoginForm class is used to create a login form for the application.
    The form contains two input fields for the username and password.
    The user can enter their credentials and submit the form to log in.
    If the credentials are correct, a success message is displayed.
    If the credentials are incorrect, an error message is displayed.
    If one or both fields are empty, a warning message is displayed.

    Attributes:
        - root: The main window of the login form
        - username_entry: The entry field for the username
        - password_entry: The entry field for the password
        - show_password: A boolean flag to toggle password visibility
        - loading_label: A label to display loading messages

    Methods:
        - initialize_items: Initializes the items on the login form (labels, entry fields, buttons)
        - toggle_password: Toggles the visibility of the password in the password entry field
        - submit_form: Validates the input fields and logs the user in
        - return_to_welcome: Closes the login form and returns to the welcome window
        - center_window: Centers the window on the screen
        - show_authentication_failed: Updates the loading label to show an authentication failure message
    """

    def __init__(self):
        # Create the main window of the login form
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.title("Login Form")
        self.username_entry = None
        self.password_entry = None
        self.show_password = False
        self.loading_label = None
        self.initialize_items()
        self.center_window(400, 200)

    def initialize_items(self):
        """
        Initialize the items on the login form:
            - Labels
            - Entry fields
            - Buttons
        The labels are used to display text on the form.
        The entry fields are used to input the username and password.
        The buttons are used to interact with the form (submit, return, show).
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
        self.password_entry = tk.Entry(form_frame, show="*", width=30)
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Create a button to toggle password visibility
        self.toggle_password_button = tk.Button(form_frame, text="Show", command=self.toggle_password)
        self.toggle_password_button.grid(row=1, column=2, padx=10, pady=5)

        # Create a frame to hold the buttons
        button_frame = tk.Frame(form_frame)
        button_frame.grid(row=2, column=0, columnspan=3, pady=10)

        # Create a return button that calls the return_to_welcome method
        return_button = tk.Button(button_frame, text="Return", command=self.return_to_welcome)
        return_button.grid(row=0, column=0, padx=10)

        # Create a submit button that calls the submit_form method
        submit_button = tk.Button(button_frame, text="Login", command=self.submit_form)
        submit_button.grid(row=0, column=1, padx=10)

        # Add a loading label but keep it hidden initially
        self.loading_label = tk.Label(self.root, text="Authenticating...", font=("Arial", 10))
        self.loading_label.pack(pady=10)
        self.loading_label.pack_forget()


    def toggle_password(self):
        """
        Toggle the visibility of the password in the password entry field.
        If the password is currently hidden, it will be shown.
        If the password is currently shown, it will be hidden.
        """
        if self.show_password:
            self.password_entry.config(show="*")
            self.toggle_password_button.config(text="Show")
        else:
            self.password_entry.config(show="")
            self.toggle_password_button.config(text="Hide")
        self.show_password = not self.show_password


    def submit_form(self):
        """
        Validate the input fields and log the user in.
        If the username or password is empty, display a warning message.
        If the credentials are correct, display a success message.
        If the credentials are incorrect, display an error message.
        """
        # Get the username and password from the entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Check if the username or password is empty
        if not username or not password:
            messagebox.showwarning("Input Error", "Please fill in both fields")
            return
        
        # Check if the username ends with '@alumchat.lol' domain
        if not username.endswith("@alumchat.lol"):
            messagebox.showerror("Invalid Username", "Username must end with '@alumchat.lol'")
            return

        # Create an instance of the EchoBot class and connect to the server
        xmpp = XMPP_Client(username, password, self)

        # Show the loading label
        self.loading_label.config(text="Authenticating...", fg="black")  # Reset label text and color
        self.loading_label.pack()
        self.loading_label.update_idletasks()

        # Connect to the server
        xmpp.connect(disable_starttls=True, use_ssl=False)
        xmpp.process(forever=False, timeout=10)
        

    def return_to_welcome(self):
        """
        Close the login form and return to the welcome window
        """
        self.root.destroy()                             # Close the login form
        from Frontend.welcome import WelcomeWindow      # Import the WelcomeWindow class
        welcome_window = WelcomeWindow()                # Recreate the welcome window
        welcome_window.root.mainloop()                  # Open the welcome window


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

    def show_authentication_failed(self):
        """
        Update the loading label to show an authentication failure message.
        """
        self.loading_label.config(text="Authentication Failed. Try again...", fg="red")
        self.loading_label.update_idletasks()

