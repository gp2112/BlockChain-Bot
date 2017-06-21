import telepot

from comandos import *


bot = telepot.Bot("409542334:AAG4DInHnEQo9O_43fqdAzxx4QdGt95xYF4")

print("Bot Iniciado!\n")


def msg_tx(msg):

    msg1 = str(msg["text"])     #texto enviado ao Bot
    cmd = msg1.split()          #divide a string em lista
    chat_id = msg["chat"]["id"] #Id do chat em List
    chat_id_Str = str(chat_id)  #ID do chat em string
    user = str(msg["from"]["username"])
    print("Id: %s / User: @%s / Texto: %s" %(chat_id_Str, user, msg1))

    if msg["text"] == "/start":     #comando de iniciar Bot
        bot.sendMessage(chat_id, "Olá! Seja bem-vindo ao Block Chain Bot beta!\n Você pode consultar transações, carteiras e blocos utilizando comandos.\nDigite /help para ver os comandos.\n\nDesenvolvido por @A4narchy")

    elif msg["text"] == "/help": #comando para mostrar comandos disponíveis
        bot.sendMessage(chat_id, "Comandos:\n /t <hash da transação>: ver informações de uma transação"
                                                    "\n /w <endereço da carteira>: ver informações de um endereço wallet"
                                                    "\n /qr <endereço>: gera QR code para endereço")
    elif cmd[0] == "/t":
        try:
            hash = str(cmd[1])      #try para caso de comando errado
            transaction(hash, chat_id, bot)         #hash será usado para definir as informações contidas no código. No caso o enderesso de transações e carteiras
        except:
            bot.sendMessage(chat_id, emoji.emojize(" :red_circle: Erro no comando! Digite /help para ver o modelo.", use_aliases=True))


    elif cmd[0] == "/w":
        try:
            hash = str(cmd[1])
            wallet(hash, chat_id, bot)          #funções disponíveis no arquivo "comandos.py"
        except:
            bot.sendMessage(chat_id, emoji.emojize(" :red_circle: Erro no comando! Digite /help para ver o modelo.", use_aliases=True))

    elif cmd[0] == "/qr":
        try:
            hash = str(cmd[1])
            qr_code(hash, bot, chat_id)
        except:
            bot.sendMessage(chat_id, emoji.emojize(" :red_circle: Erro no comando! Digite /help para ver o modelo.", use_aliases=True))

bot.message_loop(msg_tx)

while True:         #Looping
    pass

    
