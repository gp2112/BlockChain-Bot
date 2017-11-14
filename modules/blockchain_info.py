import requests
from modules.convertions import satoshi_btc, off_list

class Transaction(object):

	def __init__(self, transaction_hash):
		self.hash = transaction_hash
		self.address_in = []
		self.address_out = [] 
		self.value = '' 
		self.fee = '' 
		self.received_date = '' 
		self.confirmations = ''

	def get_info(self):
		request = requests.get("https://api.blockcypher.com/v1/btc/main/txs/%s" %self.hash).json()

		self.value = satoshi_btc(float(request["total"]))
		self.fee = satoshi_btc(request["fees"])
		self.received_date =  request['received']
		self.confirmations = request['confirmations']
		
		for i in request['inputs']:
			self.address_in.append(i["addresses"][0])

		for i in request['outputs']:
			self.address_out.append(i["addresses"][0])

		self.address_in = off_list(self.address_in)
		self.address_out = off_list(self.address_out)


class Wallet(object):
	def __init__(self, address):
		self.address = address 
		self.total_sent = '' 
		self.total_received = '' 
		self.balance = '' 
		self.unconfirmed_balance = ''
		self.unconfirmed_transactions = ''
		self.confirmed_transactions = ''

	def get_info(self):
		request = requests.get("https://api.blockcypher.com/v1/btc/main/addrs/%s" %self.address).json()

		self.total_sent = satoshi_btc(request['total_sent'])
		self.total_received = satoshi_btc(request['total_received'])
		self.balance = satoshi_btc(request['balance'])
		self.unconfirmed_balance = satoshi_btc(request['unconfirmed_balance'])
		self.unconfirmed_transactions = request['unconfirmed_n_tx']
		self.confirmed_transactions = request['final_n_tx']

class Fee(object):
	
	def __init__(self):
		self.fastest = ''
		self.halfhour = ''
		self.hour = ''

	def get_info(self):
		request = requests.get('https://bitcoinfees.earn.com/api/v1/fees/recommended').json()

		self.fastest = request['fastestFee']
		self.halfhour = request['halfHourFee']
		self.hour = request['hourFee']
