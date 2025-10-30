from users import User
from chat import PrivateChat, GroupChat
from messages import TextMessage, MediaMessage
from enums import MediaType

if __name__ == "__main__":
    # Create users
    varun = User("001", "Varun", "+917474747474")
    anuj = User("002", "Anuj", "+919876543210")

    # 1:1 Chat Example
    private_chat = PrivateChat("C1", varun, anuj)
    msg1 = TextMessage("M1", varun, "Hey Anuj! How are you?")
    varun.send_message(private_chat, msg1)

    # Group Chat Example
    group_chat = GroupChat("G1", "Weekend Plans", varun)
    group_chat.add_participant(anuj)
    msg2 = MediaMessage("M2", varun, "pic.jpg", MediaType.IMAGE)
    varun.send_message(group_chat, msg2)

    print("\nChat History (Group):", group_chat.get_chat_history())
