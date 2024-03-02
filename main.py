# from flask import request
# from fastapi import FastAPI
# import logging

# app = FastAPI()

# @app.route('/webhook', methods=['GET', 'POST'])
# def webhook():
#     logging.info('Madhukant started....................................')
#     logging.info(f'Request Came 1 => {request.method}')
#     logging.info(f'Request Came 2=> {str(request.get_data())}')
#     try:
#         if request.method == 'GET':
#             # Verification process
#             verify_token = request.args.get('hub.verify_token')
#             if verify_token == 'random-code-here-there-no-where':
#                 return request.args.get('hub.challenge')
#             return 'Invalid verification token'

#         elif request.method == 'POST':
#             # Handling incoming messages
#             data = request.get_json()
#             logging.info(f"data=> {data}")
#             if data['object'] == 'page':
#                 for entry in data['entry']:
#                     for messaging_event in entry['messaging']:
#                         sender_id = messaging_event['sender']['id']
#                         recipient_id = messaging_event['recipient']['id']
#                         if messaging_event.get('message'):
#                             # Handle incoming message
#                             message_text = messaging_event['message']['text']

#                             logging.info(f"message_text=> {message_text}")
#                             # Process the message
#                             # You can add your custom logic here
#                             send_message(sender_id, "Echo: " + message_text)  # Echo back the received message
#                         # You can handle other types of events like postbacks, etc.
#             return 'OK'
#     except Exception as e:
#         logging.info(f'Error Came while serving with Error => {e}')
#         return f'Error Came -> {e}'

# @app.route('/health', methods=['GET'])
# def health_check():
#     # Add your health check logic here
#     # For example, check if the database connection is available
#     # If everything is fine, return 200 OK
#     return 'OK', 200


# def send_message(recipient_id, message_text):
#     # Send message back to Facebook user
#     # You need to implement this based on Facebook Messenger API
#     # This can involve making HTTP requests to Facebook's API
#     pass


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi import requests

app = FastAPI()

class Message(BaseModel):
    text: str

@app.get("/webhook")
def verify_webhook(hub_verify_token: str):
    # Verification process
    if hub_verify_token == 'your_verify_token':
        return requests.args.get('hub.challenge')
    else:
        raise HTTPException(status_code=403, detail="Invalid verification token")

@app.post("/webhook")
async def handle_webhook(message: Message):
    try:
        # Handling incoming messages
        message_text = message.text
        print('message_text=>', message_text)
        # Process the message
        # You can add your custom logic here
        # send_message(sender_id, "Echo: " + message_text)  # Echo back the received message
        return 'OK'
    except Exception as e:
        print(f'Error Came while serving with Error => {e}')
        return f'Error Came -> {e}'

@app.get("/health")
def health_check():
    # Add your health check logic here
    # For example, check if the database connection is available
    # If everything is fine, return 200 OK
    resp = 'OK'
    return resp

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
