import requests
import emoji

def mercadoBitcoin_brl(bot, chat_id):
    info_r = requests.get("https://www.mercadobitcoin.net/api/ticker/")
    info = info_r.json()
    rate = int(info["ticker"]["last"])
    alta = int(info["ticker"]["high"])
    baixa = int(info["ticker"]["low"])
    bot.sendMessage(chat_id, emoji.emojize(":chart_with_upwards_trend: Alta: %d BRL\n:on: Atual: %d BRL\n:chart_with_downwards_trend: Baixa: %d BRL"%(alta, rate, baixa), use_aliases=True))

def coinDesk_usd(chat_id, bot):
    info_r = requests.get("http://api.coindesk.com/v1/bpi/currentprice.json")
    info = info_r.json()
    rate = info["bpi"]["USD"]["rate"]
    bot.sendMessage(chat_id, emoji.emojize(":dollar: Cotação Atual: %s USD" %rate, use_aliases=True))

def coinDesk_eur(chat_id, bot):
    info_r = requests.get("http://api.coindesk.com/v1/bpi/currentprice.json")
    info = info_r.json()
    rate = info["bpi"]["EUR"]["rate"]
    bot.sendMessage(chat_id, emoji.emojize(":euro: Cotação Atual: %s EUR" %rate, use_aliases=True))
