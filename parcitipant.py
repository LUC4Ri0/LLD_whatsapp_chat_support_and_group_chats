from datetime import datetime

class ChatParticipant:
    def __init__(self, user, role):
        self.user = user
        self.role = role
        self.joined_at = datetime.now()   
