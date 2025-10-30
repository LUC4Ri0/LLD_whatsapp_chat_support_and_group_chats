
from datetime import datetime

from enums import ParticipantRole
from parcitipant import ChatParticipant


class Chat:
    def __init__(self, chat_id: str):
        self.chat_id = chat_id
        self.created_at = datetime.now()
        self.participants = []
        self.messages = []
        
    def send_message(self, sender, content: str):
        self.messages.append(content)
        for participant in self.participants:
            if participant.user != sender:
                participant.user.receive_message(content)
                
    def add_participant(self, user, role=ParticipantRole.MEMBER):
        participant = ChatParticipant(user, role)
        self.participants.append(participant)
        user.join_chat(self)
        
    def remove_participant(self, user):
        self.participants = [p for p in self.participants if p.user != user]
        user.leave_chat(self)
        
    def get_chat_history(self):
        return [msg.content for msg in self.messages]
    

class PrivateChat(Chat):
    def __init__(self, chat_id: str, user1, user2):
        super().__init__(chat_id)
        self.user1 = user1
        self.user2 = user2
        self.add_participant(user1)
        self.add_participant(user2)


class GroupChat(Chat):
    def __init__(self, chat_id: str, group_name, admin):
        super().__init__(chat_id)
        self.group_name = group_name
        self.group_icon = None
        self.description = ""
        self.add_participant(admin, ParticipantRole.ADMIN)

    def set_admin(self, user):
        for participant in self.participants:
            if participant.user == user:
                participant.role = ParticipantRole.ADMIN

    def change_group_name(self, group_name: str):
        self.group_name = group_name

    def change_group_icon(self, icon_url: str):
        self.group_icon = icon_url