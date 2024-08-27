import tkinter as tk
from tkinter import messagebox

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

    Methods:
        - initialize_items: Initializes the items on the login form (labels, entry fields, buttons)
        - toggle_password: Toggles the visibility of the password in the password entry field
        - submit_form: Validates the input fields and logs the user in
        - return_to_welcome: Closes the login form and returns to the welcome window
        - center_window: Centers the window on the screen
    """

    def __init__(self):
        # Create the main window of the login form
        self.root = tk.Tk()
        self.root.title("Login Form")
        self.username_entry = None
        self.password_entry = None
        self.show_password = False
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
        self.username_entry = tk.Entry(form_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        # Create a label for the password field
        password_label = tk.Label(form_frame, text="Password:")
        password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = tk.Entry(form_frame, show="*")
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
        # TODO: Implement the submit_form method to validate the input fields and log the user in
        # Currently, the method displays a success message if the username is "test" and the password is "password"

        # Get the username and password from the entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Check if the username or password is empty
        if not username or not password:
            messagebox.showwarning("Input Error", "Please fill in both fields")
            return

        # Dummy check for successful login
        if username == "test" and password == "password":
            messagebox.showinfo("Success", "Logged in successfully!")
        else:
            messagebox.showerror("Login Failed", "Invalid credentials or failed to connect")


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

