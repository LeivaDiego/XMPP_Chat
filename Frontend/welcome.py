import tkinter as tk

class WelcomeWindow:
    """
    This class represents the welcome window of the application.
    This window will be the first thing the user sees when they run the application.

    The window contains the following buttons:
        - Register: Opens the registration form
        - Login: Opens the login form
        - Quit: Closes the application

    Attributes:
        - root: The main window of the application

    Methods:
        - initialize_items: Initializes the items on the window (labels, buttons)
        - open_register_form: Opens the registration form
        - open_login_form: Opens the login form
        - center_window: Centers the window on the screen
    """

    def __init__(self):
        # Create the main window of the application
        self.root = tk.Tk()
        self.root.title("XMPP Chat App")
        self.center_window(300, 250)
        self.root.resizable(False, False)
        self.initialize_items()

    def initialize_items(self):
        """
        Initialize the items on the welcome window:
            - Labels
            - Buttons
        The labels are used to display text on the window.
        The buttons are used to interact with the application (register, login, quit).
        """
        # Create a label to display a welcome message
        label = tk.Label(self.root, text="Welcome to XMPP Chat", font=("Arial", 14))
        label.pack(pady=20)

        # Create a frame to hold the buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # Create a login button that calls the open_login_form method
        login_button = tk.Button(button_frame, text="Login", command=self.open_login_form)
        login_button.grid(row=0, column=0, padx=10, pady=10)

        # Create a register button that calls the open_register_form method
        register_button = tk.Button(button_frame, text="Register", command=self.open_register_form)
        register_button.grid(row=1, column=0, padx=10, pady=10)

        # Create a quit button that closes the application
        quit_button = tk.Button(button_frame, text="Quit", command=self.root.destroy) # Using destroy method to close the window safely
        quit_button.grid(row=2, column=0, columnspan=2, pady=10)

    def open_register_form(self):
        self.root.destroy()                         # Close the welcome window
        from Frontend.register import RegisterForm  # Import the RegisterForm class
        register_form = RegisterForm()              # Create an instance of the RegisterForm class
        register_form.root.mainloop()               # Open the registration form

    def open_login_form(self):
        """
        Open the login form when the login button is clicked.
        """
        self.root.destroy()                     # Close the welcome window
        from Frontend.login import LoginForm    # Import the LoginForm class
        login_form = LoginForm()                # Create an instance of the LoginForm class
        login_form.root.mainloop()              # Open the login form

    def center_window(self, width, height):
        """
        Center the window on the screen based on the width and height provided.
        Calculates the x and y coordinates to position the window in the center of the
        screen based on the screen width and height.
        """
        screen_width = self.root.winfo_screenwidth()    # Get the screen width and height
        screen_height = self.root.winfo_screenheight()  # Get the screen height
        
        # Calculate the x and y coordinates to center the window
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
