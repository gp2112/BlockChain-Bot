import telepot
from modules.send import send_commands

try:
    bot = telepot.Bot('409542334:AAGZ-iKmWg4nrWSxe50LCu4WUY9LpTvl594')

    print("Bot Iniciado!\n")

    def handle(msg):
        print(msg['text'])
        send_commands(bot, msg)


    bot.message_loop(handle)

    while True:
        pass

except KeyboardInterrupt:
    pass