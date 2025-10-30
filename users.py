from datetime import datetime


class User:
    def __init__(self, uid: str, name: str, phone_no: str):
        self.uid = uid
        self.name = name
        self.phone_no = phone_no
        self.status = "Hey there! I am using ChatApp."
        self.last_seen = datetime.now()
        self.chats = []

    def send_message(self, chat, message: str):
        chat.send_message(self, message)

    def receive_message(self, message: str):
        print(f"New message for {self.name}: {message}")
        
    def join_chat(self, chat):
        self.chats.append(chat)
        
    def leave_chat(self, chat):
        if chat in self.chats:
            self.chats.remove(chat)
        