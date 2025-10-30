from users import User
from chat import PrivateChat, GroupChat
from messages import TextMessage, MediaMessage
from enums import MediaType

if __name__ == "__main__":
    # Create users
    alice = User("U1", "Alice", "+911234567890")
    bob = User("U2", "Bob", "+919876543210")

    # 1:1 Chat Example
    private_chat = PrivateChat("C1", alice, bob)
    msg1 = TextMessage("M1", alice, "Hey Bob! How are you?")
    alice.send_message(private_chat, msg1)

    # Group Chat Example
    group_chat = GroupChat("G1", "Weekend Plans", alice)
    group_chat.add_participant(bob)
    msg2 = MediaMessage("M2", alice, "pic.jpg", MediaType.IMAGE)
    alice.send_message(group_chat, msg2)

    print("\nChat History (Group):", group_chat.get_chat_history())
