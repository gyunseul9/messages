# -*- coding: utf-8 -*- 
import requests
import time
import sys
from config import Configuration
from text import Text
from slacker import Slacker
import telegram

class Messages:

	def __init__(self,kind):
		self.kind = kind

	def set_params(self):
		self.kind = sys.argv[1]

	def validate(self):
		default	= {
			'kind':'slack'
		}

		self.kind = default.get('kind')	if self.kind == '' else self.kind.lower()

	def send_slack(self):

		text = Text.get_text('slack')	

		attachments_dict = dict()
		attachments_dict['text'] = text
		attachments = [attachments_dict]

		token = Configuration.get_token('slack')
		slack = Slacker(token[1])
		slack.chat.post_message(channel=token[0], text=None, attachments=attachments, as_user=True)

	def send_teams(self):

		text = Text.get_text('teams')	

		token = Configuration.get_token('teams')

		headers = {
		    'Content-Type': 'Application/JSON;charset=utf-8',
		}

		card = 'MessageCard'
		color = '0072C6'
		title = ''

		data = '{"@context":"'+token[0]+'","@type":"'+card+'","themeColor":"'+color+'","title":"'+title+'","text":"'+text+'"}'

		response = requests.post(token[1], headers=headers, data=data.encode('utf-8'))

	def send_telegram(self):
		
		text = Text.get_text('telegram')
		
		token = Configuration.get_token('telegram')
		user = Configuration.get_user('lonbebot')
	
		bot = telegram.Bot(token=token[0])

		for key, value in user.items():
			print(key, value)
			bot.sendMessage(chat_id=key, text=text)

	def execute(self):

		self.validate()

		try:

			if self.kind == 'telegram':
				self.send_telegram()
			elif self.kind == 'teams':
				self.send_teams()
			elif self.kind == 'slack':
				self.send_slack()
			else:
				self.send_slack()
			
		except Exception as e:
			with open('./error.log','a') as file:
				file.write('{} You got an error: {}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),str(e)))

def run():
	messages = Messages('')
	messages.set_params()
	messages.execute()

if __name__ == "__main__":
	run()
