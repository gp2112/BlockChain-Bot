import telepot
from comandos import *

bot = telepot.Bot("TOKEN")

print("Bot Iniciado!\n")


def msg_tx(msg):
    print(msg)
    msg1 = str(msg["text"])     #texto enviado ao Bot
    cmd = msg1.split()          #divide a string em lista
    chat_id = msg["chat"]["id"]     #ID do chat

    if msg["text"] == "/start":     #comando de iniciar Bot
        bot.sendMessage(chat_id, "Olá! Seja bem-vindo ao Block Chain Bot beta!\n Você pode consultar transações, carteiras e blocos utilizando comandos.\nDigite /help para ver os comandos.\n\nDesenvolvido por @A4narchy")

    elif msg["text"] == "/help": #comando para mostrar comandos disponíveis
        bot.sendMessage(chat_id, "Comandos:\n /t <hash da transação>: ver informações de uma transação"
                                                    "\n /w <enderesso da carteira>: ver informações de um endereçoo wallet"
                                                    "\n /qr <enderesso>: gera QR code para endereço")
    elif cmd[0] == "/t":
        hash = str(cmd[1])                      #hash será usado para definir as informações contidas no código. No caso o enderesso de transações e carteiras
        try:
            transaction(hash, chat_id, bot)
        except:
            bot.sendMessage(chat_id, emoji.emojize(" :red_circle: Erro no comando! Digite /help para ver o modelo.", use_aliases=True))


    elif cmd[0] == "/w":
        hash = str(cmd[1])
        try:
            wallet(hash, chat_id, bot)          #funções disponíveis no arquivo "comandos.py"
        except:
            bot.sendMessage(chat_id, emoji.emojize(" :red_circle: Erro no comando! Digite /help para ver o modelo.", use_aliases=True))

    elif cmd[0] == "/qr":
        hash = str(cmd[1])
        try:
            qr_code(hash, bot, chat_id)
        except:
            bot.sendMessage(chat_id, emoji.emojize(" :red_circle: Erro no comando! Digite /help para ver o modelo.", use_aliases=True))

bot.message_loop(msg_tx)

while True:         #Looping
    pass

    
