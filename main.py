from Frontend.welcome import WelcomeWindow
import platform
import asyncio

def main():
    if platform.system() == 'Windows':
        # On Windows, the proactor event loop is necessary to listen for
        # events on stdin while running the asyncio event loop.
        print("INFO: The current platform is Windows")
        if hasattr(asyncio, 'WindowsSelectorEventLoopPolicy'):
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # Create the welcome window and start the main loop
    welcome_window = WelcomeWindow()
    welcome_window.root.mainloop()

if __name__ == "__main__":
    main()