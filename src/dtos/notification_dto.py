class User:
    def __init__(self, id, name, email, phone_number, subscribed, channels):
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.subscribed = subscribed
        self.channels = channels

class NotificationDTO:
    def __init__(self, user: User, category: str, message: str, channels: list):
        self.user = user
        self.category = category
        self.message = message
        self.channels = channels
