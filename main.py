import requests

# Final configuration
phone_number = '+351913221808'
image_url = 'https://i.postimg.cc/NFmkX9LC/1768346889340.png'
message_text = f'Reminder to take your vitamins! Love you. {image_url}'

def send_text():
    response = requests.post('https://textbelt.com/text', {
        'number': phone_number,
        'message': message_text,
        'key': 'textbelt',
    })

    result = response.json()

    if result.get('success'):
        print(f"Success! Message sent to {phone_number}")
        print(f"Quota remaining: {result.get('quotaRemaining')}")
    else:
        print(f"Failed: {result.get('error')}")

if __name__ == "__main__":
    send_text()