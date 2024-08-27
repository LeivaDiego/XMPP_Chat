import tkinter as tk

class HomeWindow:
    """
    The HomeWindow class is used to create a home window for the application.
    The home window is displayed after the user has successfully logged in.
    """
    # TODO: Implement the HomeWindow class to create a home window for the application
    # Currently, the HomeWindow class is a placeholder and does not contain any functionality.

    def __init__(self, xmpp_client):
        self.root = tk.Tk()
        self.root.title("XMPP Chat Home")
        self.root.resizable(False, False)
        self.center_window(600, 200)
        self.client = xmpp_client
        label = tk.Label(self.root, text="Welcome to XMPP Chat Home Page you are now logged in!", font=("Arial", 14))
        label.pack(pady=20)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def logout(self):
        self.client.disconnect()
        print("INFO: Client disconnected from the server")
        self.root.destroy()
        print("INFO: Please wait while tasks are being cleaned up")

    def on_close(self):
        self.logout()
