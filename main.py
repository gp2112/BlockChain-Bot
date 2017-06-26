import telepot
from cotacao import *
from comandos import *


bot = telepot.Bot("TOKEN")

print("Bot Iniciado!\n")


def msg_tx(msg):

    try:
        msg1 = str(msg["text"])     #texto enviado ao Bot
        cmd = msg1.split()          #divide a string em lista
        chat_id = msg["chat"]["id"] #Id do chat em List
        chat_id_Str = str(chat_id)  #ID do chat em string
        user = str(msg["from"]["username"])
        print("Id: %s / User: @%s / Texto: %s" %(chat_id_Str, user, msg1))

        bot.sendMessage('''Id do grupo''', "Id: %s\nUser: @%s\nTexto: %s" %(chat_id_Str, user, msg1))
    
    except:
        print("Erro de conexão")

    if msg["text"] == "/start":     #comando de iniciar Bot
        bot.sendMessage(chat_id, "Olá! Seja bem-vindo ao Block Chain Bot beta!\n Você pode consultar transações, carteiras e blocos utilizando comandos.\nDigite /help para ver os comandos.\n\nDesenvolvido por @A4narchy")

    elif msg["text"] == "/help": #comando para mostrar comandos disponíveis
        bot.sendMessage(chat_id, "Comandos:\n /t <hash da transação>: ver informações de uma transação"
                                                    "\n\n /w <endereço da carteira>: ver informações de um endereço wallet"
                                                    "\n\n /qr <endereço>: gera QR code para endereço"
                                                    "\n\n /fee : veja as taxas de transação recomendadas ou use \n/fee <nº de endereços de saída> <nº de endereços de entrada> "
                                                    "para estimar a quantidade de bytes em sua transação e calcuar uma taxa apropriada.\nExemplo: /fee 3 2"
                                                    "\n\n/cotacao <moeda> : Veja cotação atual em reais, dólar ou euro.\nEx: /cotacao brl"
                                                    "\n\n /feedback <mensagem> : mande sugestões, elogios, informações de bugs e outros ao desenvolvedor")
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

    elif cmd[0] == "/fee": #fee recomendada em satoshi/byte ou recomendada de acordo com o tamanho de byte da transação, em bitcoin
        fee(chat_id, bot, cmd)

    elif cmd[0] == "/rate":              #Cotações
        try:
            if cmd[1] == "brl" or cmd[1] == "BRL" or cmd[1] == "real":                     #cotação em BRL
                mercadoBitcoin_brl(bot, chat_id)
            elif cmd[1] == "usd" or cmd[1] == "USD" or cmd[1] == "dólar":                      #cotação em USD
                coinDesk_usd(chat_id, bot)
            elif cmd[1] == "eur" or cmd[1] == "EUR" or cmd[1] == "euro":    #cotação em EUR
                coinDesk_eur(chat_id, bot)
        except:bot.sendMessage(chat_id, emoji.emojize(" :red_circle: Erro no comando! Digite /help para ver o modelo.", use_aliases=True))

    elif cmd[0] == "/qr":       #Comando para gerar QR code
        try:
            hash = str(cmd[1])
            qr_code(hash, bot, chat_id)
        except:
            bot.sendMessage(chat_id, emoji.emojize(" :red_circle: Erro no comando! Digite /help para ver o modelo.", use_aliases=True))

    elif cmd[0] == "/feedback":         #Enviar Feedback ao desenvolverdor
        bot.sendMessage(chat_id, "Feedback enviado!\nObrigado pela colaboração!")
        bot.sendMessage('''sua ID''', "Feedback de @%s: \"%s\"" %(user, msg["text"]))

bot.message_loop(msg_tx)

while True:         #Looping
    pass


