from enum import Enum

class ParticipantRole(Enum):
    ADMIN = "ADMIN"
    MEMBER = "MEMBER"

class MessageStatus(Enum):
    SENT = "SENT"
    DELIVERED = "DELIVERED"
    READ = "READ"

class MediaType(Enum):
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"
    AUDIO = "AUDIO"
    DOCUMENT = "DOCUMENT"

