from control import *

bot = telepot.Bot("427813816:AAGY-SaRHLp7U_sPBvmV8VN2P7LlOkyBFPU")

print("Bot Iniciado!\n")

def handle(msg):
    ct, chat_type, chat_id = telepot.glance(msg)
    user = str(msg["from"]["username"])
    text = msg["text"]
    print("Id: %s / User: @%s / Texto: %s" %(chat_id, user, text))
    logs(msg, user)
    start(text, chat_id, bot, user)
    transaction(text, chat_id, bot)
    wallet(text, chat_id, bot)
    fee(chat_id, bot, text)
    rate(text, bot, chat_id)
    qr_code(text, bot, chat_id)


bot.message_loop(handle)

while True:
    pass
