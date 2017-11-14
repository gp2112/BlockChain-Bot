import telepot
from modules.send import send_commands

try:
    bot = telepot.Bot('TOKEN')

    print("Bot Iniciado!\n")

    def handle(msg):
        print(msg['text'])
        send_commands(bot, msg)


    bot.message_loop(handle)

    while True:
        pass

except KeyboardInterrupt:
    pass
