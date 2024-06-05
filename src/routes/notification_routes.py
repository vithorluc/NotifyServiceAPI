from flask import Blueprint, request, jsonify
from src.services.notification_service import NotificationService

notification_bp = Blueprint('notification', __name__)
notification_service = NotificationService()

@notification_bp.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    category = data.get('category')
    message = data.get('message')
    if not category or not message:
        return jsonify({'error': 'Category and message are required'}), 400
    notification_service.send_notification(category, message)
    return jsonify({'message': 'Notification sent successfully'}), 200
