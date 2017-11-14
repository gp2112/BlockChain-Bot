import telepot
import emoji
from modules.blockchain_info import *

class Command(object):

	def __init__(self, msg):
		self.user = msg['from']['username']
		self.content_type, self.chat_type, self.chat_id = telepot.glance(msg)
		self.text = msg['text']

	def start(self):
		return "Olá %s, bem-vindo ao BlockChain Bot!\n Digite /help para ver os comandos e opções." %self.user

	def transaction(self):
		transaction_hash = self.text.split(' ')[1]
		transaction = Transaction(transaction_hash)
		transaction.get_info()
		return emoji.emojize('''Recebido em: %s\n\n :outbox_tray:Endereços de Saída: %s
					:inbox_tray:Endereços de Entrada: %s \n\n :money_with_wings:Valor enviado: %f btc
					:small_red_triangle_down:Taxa: %f btc\n\n  :white_check_mark:Confirmações: %s\n\n\n
					:information_source:Informações por Blockcypher.com''' %(transaction.received_date, transaction.address_in, transaction.address_out, transaction.value, transaction.fee, transaction.confirmations), use_aliases=True)

	def wallet(self):
		wallet_address = self.text.split(' ')[1]
		wallet = Wallet(wallet_address)
		wallet.get_info()

		return emoji.emojize(''' Endereço: %s \n\n:moneybag: Saldo: %f btc \n\n:money_with_wings: Total Recebido: %f btc \n\n:white_circle: Saldo não confirmado: %f btc\n
							:white_check_mark: Nº de transações confirmadas: %d \n\n:x: Transações não confirmadas: %d ''' %(wallet.address, wallet.balance, wallet.total_received, wallet.unconfirmed_balance, wallet.confirmed_transactions, wallet.unconfirmed_transactions), use_aliases=True)

	def fee(self):
		fee = Fee()
		fee.get_info()
		
		return emoji.emojize(":clock1: Taxa mais rápida: \n%d sts/byte\n\n:clock130: Confirma em cerca de 30 min: %d sts/byte\n\n:clock2: Confirma em cerca de 1h: \n%d sts/byte" %(fee.fastest, fee.halfhour, fee.hour), use_aliases=True)	