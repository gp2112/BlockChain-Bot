import telepot
import requests

bot = telepot.Bot("TOKEN")

print("Bot Iniciado!\n")


def msg_tx(msg):
    print(msg)
    msg1 = str(msg["text"])
    cmd = msg1.split()
    if msg["text"] == "/start":
        bot.sendMessage(msg["chat"]["id"], "Olá! Seja bem-vindo ao Block Chain Bot beta!\n Você pode consultar transações, carteiras e blocos utilizando comandos.\nDigite /help para ver os comandos.\n\nDesenvolvido por @A4narchy")
    elif msg["text"] == "/help":
        bot.sendMessage(msg["chat"]["id"], "Comandos:\n /t <hash da transação>: ver informações de uma transação"
                                                    "\n Outros em breve")
    elif cmd[0] == "/t":
        hash = str(cmd[1])
        info_r = requests.get("https://api.blockcypher.com/v1/btc/main/txs/%s" %hash)
        info = info_r.json()
        adress_in = info["addresses"][1]
        adress_in1 = str(adress_in)
        adress_out = info["addresses"][0]
        adress_out1 = str(adress_out)
        valor_r1 = info["total"]
        valor_r2 = float(valor_r1)*0.00000001
        fee1 = float(info["fees"])*0.00000001
        valor_env =  valor_r2 + fee1
        receiv = info["received"]
        receiv1 = str(receiv)
        conf = info["confirmations"]
        conf1 = str(conf)
        bot.sendMessage(msg["chat"]["id"], "Recebido em: %s\n\n Endereço de Saída: %s \n\n Endereço de Entrada: %s \n\n Valor enviado: %f btc\n\n Valor recebido: %f btc\n\n Taxa: %f btc\n\n  Confirmações: %s\n\n\n Informações por Blockcypher.com" %(receiv1, adress_in1, adress_out1, valor_env, valor_r2, fee1, conf))

bot.message_loop(msg_tx)

while True:
    pass

    
