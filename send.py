import telepot

def sendpicture(message,image):
    bot = telepot.Bot('6177243905:AAFqwIx5NCPznKv3pXJ8sT-6ibUKVm_VM5o')
    bot.sendPhoto(5046094109, photo=open(image, 'rb'))
    bot.sendMessage(5046094109, message)