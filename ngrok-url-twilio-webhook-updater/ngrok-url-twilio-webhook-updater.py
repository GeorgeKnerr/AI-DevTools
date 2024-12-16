import subprocess
import time
import requests
from twilio.rest import Client
import os

# ngrok log file
NGROK_LOG_FILE = "ngrok.log"

def start_ngrok(port=5050, log_file=NGROK_LOG_FILE):
    """
    Check if ngrok is already running. If not, start it in the background.
    """
    try:
        # Check if ngrok is already running
        response = requests.get("http://127.0.0.1:4040/api/tunnels")
        if response.status_code == 200:
            print("ngrok is already running.")
            return  # Skip starting a new ngrok instance
        
        # Remove existing log file
        if os.path.exists(log_file):
            os.remove(log_file)
        
        # Start ngrok and redirect output to the log file
        with open(log_file, "w") as log:
            subprocess.Popen(["ngrok", "http", str(port)], stdout=log, stderr=subprocess.STDOUT)
        print(f"ngrok started. Logs are being written to '{log_file}'")
        
        # Wait for ngrok to initialize
        time.sleep(3)  # Give ngrok some time to start
    except requests.ConnectionError:
        print("ngrok is not running. Starting a new instance.")
    except Exception as e:
        print(f"Error starting ngrok: {e}")

def get_ngrok_url():
    """
    Retrieve the public HTTPS URL from the local ngrok API.
    """
    try:
        response = requests.get("http://127.0.0.1:4040/api/tunnels")
        tunnels = response.json().get("tunnels", [])
        for tunnel in tunnels:
            if tunnel.get("public_url").startswith("https"):
                return tunnel["public_url"]
    except Exception as e:
        print(f"Error fetching ngrok URL: {e}")
    return None

def update_twilio_webhook(ngrok_url):
    """
    Update Twilio phone number webhook with the provided ngrok URL.
    """
    try:
        # Load Twilio credentials from environment variables
        TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
        TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
        TWILIO_PHONE_SID = os.getenv("TWILIO_PHONE_SID")

        if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_SID]):
            raise EnvironmentError("Missing Twilio environment variables. Set TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and TWILIO_PHONE_SID.")

        # Initialize Twilio client
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # Update webhook
        client.incoming_phone_numbers(TWILIO_PHONE_SID).update(
            sms_url=f"{ngrok_url}/sms",
            voice_url=f"{ngrok_url}/voice"
        )
        print(f"Twilio webhook updated to: {ngrok_url}")
    except Exception as e:
        print(f"Error updating Twilio webhook: {e}")

def run_ngrok_and_update_twilio(port=5050):
    """
    Complete process: Start ngrok, fetch the URL, and update Twilio webhook.
    """
    start_ngrok(port)
    ngrok_url = None
    
    # Retry fetching the ngrok URL up to 5 times
    for attempt in range(5):
        ngrok_url = get_ngrok_url()
        if ngrok_url:
            break
        print("Waiting for ngrok URL...")
        time.sleep(2)
    
    if ngrok_url:
        print(f"ngrok Public URL: {ngrok_url}")
        update_twilio_webhook(ngrok_url)
    else:
        print("Failed to retrieve ngrok URL. Check ngrok logs for errors.")

# If used as a standalone script
if __name__ == "__main__":
    run_ngrok_and_update_twilio(port=5050)
