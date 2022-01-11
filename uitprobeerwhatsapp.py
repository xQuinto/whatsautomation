from whatsapp import WhatsApp
whatsapp = WhatsApp(100, session="mysession")
user_names = whatsapp.unread_usernames(scrolls=20)
for name in user_names:
    messages = whatsapp.get_last_message_for("Vinnie <3")
    print(messages)
    #messgaes_len = len(messages)
    #latest_msg = messages[messgaes_len]