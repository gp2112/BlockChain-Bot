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

#Função para enviar QR code em imagem para user
def qr_code(hash, bot, chat_id):
    bot.sendPhoto(chat_id, "https://api.qrserver.com/v1/create-qr-code/?size=460x320&data=%s" %hash)