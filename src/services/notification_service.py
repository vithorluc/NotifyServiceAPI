from app.repositories.log_repository import LogRepository
from app.dtos.notification_dto import NotificationDTO
from app.services.sms_service import SMSService
from app.services.email_service import EmailService
from app.services.push_service import PushService

class NotificationService:
    def __init__(self):
        self.log_repository = LogRepository()
        self.sms_service = SMSService()
        self.email_service = EmailService()
        self.push_service = PushService()

    def send_notification(self, notification: NotificationDTO):
        channels = notification.channels
        for channel in channels:
            if channel == 'SMS':
                self.sms_service.send(notification)
            elif channel == 'EMAIL':
                self.email_service.send(notification)
            elif channel == 'PUSH':
                self.push_service.send(notification)
        self.log_repository.log(notification)
