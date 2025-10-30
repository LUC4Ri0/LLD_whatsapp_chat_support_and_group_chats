from datetime import datetime

from enums import MediaType, MessageStatus


class Message:
    def __init__(self, message_id: str, sender, content: str):
        self.message_id = message_id
        self.sender = sender
        self.content = content
        self.timestamp = datetime.now()
        self.status = MessageStatus.SENT
        
    def edit(self, new_content: str):
        self.content = new_content
        
    def delete(self):
        self.content = "[This message has been deleted]"
        

class TextMessage(Message):
    def __init__(self, message_id: str, sender, content: str):
        super().__init__(message_id, sender, content)


class MediaMessage(Message):
    def __init__(self, message_id: str, sender, media_url: str, media_type: MediaType):
        super().__init__(message_id, sender, f"Media: {media_url}")
        self.media_url = media_url
        self.media_type = media_type
