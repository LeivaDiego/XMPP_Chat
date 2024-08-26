import asyncio
import platform
import signal
from client import XMPPClient
from view import display_menu

# Fix for Windows event loop policy error
if platform.system() == 'Windows':
    # If running on Windows, set the event loop policy to use the SelectorEventLoop
    if hasattr(asyncio, 'WindowsSelectorEventLoopPolicy'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def signal_handler(signal, frame):
    # Signal handler to stop the client when a signal is received
    print("Signal received, stopping the client...")
    loop = asyncio.get_event_loop()
    for task in asyncio.all_tasks(loop):
        task.cancel()
    loop.stop()

def main():
    # Display menu and get user choice
    display_menu()
    choice = input("Choose an option: ")

    # Process user choice and call appropriate functions
    if choice == "1":
        # Login option selected
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        client = XMPPClient(username, password)
        client.connect_and_run()

    elif choice == "2":
        # Register option selected
        username = input("Enter a username to register: ")
        password = input("Enter a password: ")
        client = XMPPClient(username, password, register=True)
        client.connect_and_run()

    elif choice == "3":
        # Exit option selected
        print("Exiting...")

    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Run the main function
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Process interrupted. Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")
