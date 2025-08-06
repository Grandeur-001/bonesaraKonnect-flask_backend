from flask import Blueprint, request, jsonify
from flask_mail import Message
from extensions import mail 

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact', methods=['POST'])
def send_contact_message():
    data = request.json

    name = data.get('name')
    email = data.get('email')
    subject = data.get('subject')
    message = data.get('message')

    if not name or not email or not subject or not message:
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        msg = Message(
            subject=f"[Contact] {subject}",
            sender=email,
            recipients=['tamunosajeminimiema@gmail.com'],
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        )
        mail.send(msg)
        return jsonify({'message': 'Message sent successfully!'}), 200
    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({'error': 'Failed to send message'}), 500
