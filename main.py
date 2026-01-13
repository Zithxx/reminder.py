import requests
import os

# Instead of the real number, we tell Python to look for a secret
phone_number = os.environ.get('MY_PHONE_NUMBER')
image_url = 'https://i.postimg.cc/NFmkX9LC/1768346889340.png'
message_text = f'Reminder to take your vitamins! Love you. {image_url}'

def send_text():
    # Safety check: make sure the secret was actually found
    if not phone_number:
        print("Error: Phone number secret not found!")
        return

    response = requests.post('https://textbelt.com/text', {
        'number': phone_number,
        'message': message_text,
        'key': 'textbelt',
    })

    result = response.json()
    if result.get('success'):
        print("Success! Message sent to the hidden number.")
    else:
        print(f"Failed: {result.get('error')}")

if __name__ == "__main__":
    send_text()
