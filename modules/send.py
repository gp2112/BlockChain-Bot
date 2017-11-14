from modules.command import Command

def send_commands(bot, msg):
	command = Command(msg)

	if command.content_type == 'text':

		if command.text.startswith('/start'):
			bot.sendMessage(command.chat_id, command.start())

		elif command.text.startswith('/t'):
			bot.sendMessage(command.chat_id, command.transaction())

		elif command.text.startswith('/w'):
			bot.sendMessage(command.chat_id, command.wallet())

		elif command.text.startswith('/fee'):
			bot.sendMessage(command.chat_id, command.fee())