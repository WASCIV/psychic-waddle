import requests
import random

API_URL = "http://195.35.23.236:5000/send-email"
API_KEY = "xGTBfUdxUEMNKiwnNf2r2CErWauJIDP94uajOWt7x8g"  # Same API key as in the server

def generate_otp():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

def send_otp_email(recipient_email, otp):
    headers = {'API-Key': API_KEY}
    data = {'recipient': recipient_email, 'otp': otp}
    response = requests.post(API_URL, json=data, headers=headers)
    return response.status_code

def verify_otp(sent_otp):
    user_otp = input("Enter the OTP you received: ")
    if user_otp == sent_otp:
        print("OTP verification successful.")
    else:
        print("Incorrect OTP. Please try again.")

def main():
    while True:
        print("\n--- OTP Sender ---")
        print("1. Send OTP")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            recipient_email = input("Enter the recipient's email: ")
            otp = generate_otp()
            status_code = send_otp_email(recipient_email, otp)
            if status_code == 200:
                print("OTP sent successfully.")
                verify_otp(otp)
            else:
                print("Failed to send OTP. Please check the server and connectivity.")
        elif choice == "2":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
