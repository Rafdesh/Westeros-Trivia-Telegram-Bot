# Python Bot Backend

import string
import json
import random
from pprint import pprint


# Token Constants

BASE_URL = 'https://api.telegram.org/bot'
TOKEN = '125579945:AAGjgsLLGeSqSILvfky71QjuMcZpeIBpuho/'
MAIN_URL = 'cURL -s -X POST' + BASE_URL + TOKEN + '-d text="A message from your bot"' + '-d chat_id="33843334"'


def sendMessage():
	print(MAIN_URL)
	# curl -s -X POST https://api.telegram.org/bot125579945:AAGjgsLLGeSqSILvfky71QjuMcZpeIBpuho/sendMessage \ -d text="A message from your bot" \ -d chat_id=33843334
	#print('curl -s -X POST https://api.telegram.org/bot125579945:AAGjgsLLGeSqSILvfky71QjuMcZpeIBpuho/sendMessage -d text="A message from your bot" -d chat_id=33843334')


json_file = 'data.json'
json_data = open(json_file)
data = json.load(json_data)

#print data['result'][0]['message']['text']


QuestionsList = [
'Does Cersei love her children?',
'Is the Hound really dead?',
'Is Jon Snow really dead?',
'Who killed Ygritte?',
'Why does Arya go blind?',
'Who is the prettiest girl in the show?'
]

arrayEnd = len(QuestionsList)

i = random.randint(0, arrayEnd)


if data['result'][0]['message']['text'] == '/question':
	#print QuestionsList[i]
	sendMessage()


'''if text.contains("/question"):
	reply = "Is Cersei dead?"
	sendMessage(chat_id,reply)
else
	reply = "False"'''

json_data.close()




# curl -s -X POST https://api.telegram.org/bot125579945:AAGjgsLLGeSqSILvfky71QjuMcZpeIBpuho/sendMessage \ -d text="A message from your bot" \ -d chat_id=33843334


