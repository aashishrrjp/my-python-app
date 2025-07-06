import os
from flask import Flask
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Get the hostname of the container
hostname = os.uname()[1]

# Define the main route
@app.route('/')
def hello_world():
    """
    Returns a simple greeting message along with server details.
    """
    # Get current server time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create the response string
    return f"""
    <h3>Hello from Ashish To 1st task :)</h3>
    <p>This response was served by pod: <b>{hostname}</b></p>
    <p>Server time: {current_time}</p>
    """

# Main entry point for the application
if __name__ == '__main__':
    # Run the app on port 5000, accessible from any network interface
    app.run(host='0.0.0.0', port=5000)
