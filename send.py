import telepot

def sendpicture(message,image):
    bot = telepot.Bot(TELEGRAM_BOT_TOKEN)
    bot.sendPhoto(TELEGRAM_CHAT_ID, photo=open(image, 'rb'))
    bot.sendMessage(TELEGRAM_CHAT_ID, message)
