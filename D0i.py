import streamlit as st
import time

# Set the timer duration
timer_duration = 30

# Set the notification message
notification_message = "Exercise is coming!"

# Create a flag to track whether the timer is running
timer_running = False

# Create a flag to track whether the app is in full screen mode
full_screen_mode = False

# Define a function to show the notification
def show_notification(message):
    st.balloons()
    st.write(message)

# Define a function to start the timer
def start_timer():
    global timer_running
    timer_running = True
    time.sleep(timer_duration)
    stop_timer()

# Define a function to stop the timer
def stop_timer():
    global timer_running
    timer_running = False

# Define a function to go full screen
def go_full_screen():
    global full_screen_mode
    full_screen_mode = True
    st.set_page_config(layout="wide")

# Define a function to go back to normal screen
def go_back_to_normal_screen():
    global full_screen_mode
    full_screen_mode = False
    st.set_page_config(layout="centered")

# Main function
def main():

    # Show the notification
    show_notification(notification_message)

    # Start the timer
    start_timer()

    # While the timer is running
    while timer_running:

        # If the app is not in full screen mode
        if not full_screen_mode:

            # Go full screen
            go_full_screen()

        # Show the timer
        st.write(timer_duration)
        timer_duration -= 1

        # Refresh the page
        st.refresh()

    # Stop the timer
    stop_timer()

    # Go back to normal screen
    go_back_to_normal_screen()

# Start the app
if __name__ == "__main__":
    main()

