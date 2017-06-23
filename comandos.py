import requests
import emoji

#função para extrair informações do enderesso de transação fornecido pelo User
def transaction(hash, chat_id, bot):
     info_r = requests.get("https://api.blockcypher.com/v1/btc/main/txs/%s" %hash)
     info = info_r.json()
     adress_in = str(info["addresses"][1])      #Endereço de entrada
     adress_out = str(info["addresses"][0])      #enderesso de saída
     valor_r1 = float(info["total"])*10**-8      #Valor total --- OBS: *10**-8 Converte de satoshi para BTC
     fee1 = float(info["fees"])*10**-8        #taxas da transação
     valor_env =  valor_r1 + fee1           #Valor total enviado (inclue taxas)
     receiv = str(info["received"])        #Data do recebimento
     conf = str(info["confirmations"])      #confirmações
     #Envia retorno ao User:
     bot.sendMessage(chat_id, emoji.emojize("Recebido em: %s\n\n :outbox_tray:Endereço de Saída: %s \n\n "
                                            ":inbox_tray:Endereço de Entrada: %s \n\n :money_with_wings:Valor enviado: %f btc\n\n "
                                            ":moneybag:Valor recebido: %f btc\n\n "
                                            ":small_red_triangle_down:Taxa: %f btc\n\n  :white_check_mark:Confirmações: %s\n\n\n "
                                            ":information_source:Informações por Blockcypher.com"
                                            %(receiv, adress_in, adress_out, valor_env, valor_r1, fee1, conf),  use_aliases=True))

#função para extrair informações do enderesso da wallet fornecido pelo User
def wallet(hash, chat_id, bot):
    info_r = requests.get("https://api.blockcypher.com/v1/btc/main/addrs/%s" %hash)
    info = info_r.json()
    t_received = float(info["total_received"])*10**-8
    balance = float(info["balance"])*10**-8
    un_balance = float(info["unconfirmed_balance"])*10**-8
    n_trans = int(info["n_tx"])
    u_trans = int(info["unconfirmed_n_tx"])
    bot.sendMessage(chat_id, emoji.emojize("Endereço: %s \n\n:moneybag: Saldo: %f btc \n\n:money_with_wings: Total Recebido: %f btc \n\n:white_circle: Saldo não confirmado: %f btc \n\n"
                                           ":white_check_mark: Nº de transações confirmadas: %d \n\n:x: Transações não confirmadas: %d" %(hash, balance, t_received, un_balance, n_trans, u_trans), use_aliases=True))

def fee(chat_id, bot, cmd):        #Mostra Fees recomendada
    info_r = requests.get("https://bitcoinfees.21.co/api/v1/fees/recommended")
    info = info_r.json()
    fastest_fee = int(info["fastestFee"])
    halfHour_fee = int(info["halfHourFee"])
    hour_fee = int(info["hourFee"])
    try:
        out = int(cmd[1]) #números de endereços de entrada                     #Mostra fees recomendadas de acordo com sua transação estimando os bytes
        inp = int(cmd[2])     #número de endereços de saída
        size = out*34 + 180*inp + 10 #tamanho estimado da transação em Bytes
        fastest_fee1 =  size * fastest_fee * 10**-8  #(Converte de satoshi para BTC)
        halfHour_fee1 = size * halfHour_fee * 10**-8
        hour_fee1 = size * hour_fee * 10**-8
        bot.sendMessage(chat_id,emoji.emojize("Sua transação está estimada em %d bytes\n\n:rocket: Taxa rápida: %f btc \n\n:bullettrain_side: Até 30min para confirmar: %f btc\n\n:turtle: Até 1h para confirmar: %f btc" %(size, fastest_fee1, halfHour_fee1, hour_fee1), use_aliases=True))

    except:
        bot.sendMessage(chat_id, emoji.emojize(":clock1: Taxa mais rápida: \n%d sts/byte\n\n:clock130: Confirma em cerca de 30 min: %d sts/byte\n\n:clock2: Confirma em cerca de 1h: \n%d sts/byte"%(fastest_fee, halfHour_fee, hour_fee), use_aliases=True))

#Função para enviar QR code em imagem para user
def qr_code(hash, bot, chat_id):
    bot.sendPhoto(chat_id, "https://api.qrserver.com/v1/create-qr-code/?size=460x320&data=%s" %hash)
