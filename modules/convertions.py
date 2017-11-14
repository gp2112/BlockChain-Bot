def satoshi_btc(satoshis):
	if isinstance(satoshis, float) or isinstance(satoshis, int):
		return satoshis * (10 ** -8)
	else:
		return 'Use integers or float variables'

def off_list(list_address):
	string = ''
	for i in range(len(list_address)):
		string += '%s \n' %list_address[i]
	return string