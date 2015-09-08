# Python Bot Backend

import string
import json
import random
import sys
import requests
from pprint import pprint
from twx.botapi import TelegramBot, ReplyKeyboardMarkup

def get_me(**kwargs):
    """
    A simple method for testing your bot's auth token. Requires no parameters.
    Returns basic information about the bot in form of a User object.
    :param \*\*kwargs: Args that get passed down to :class:`TelegramBotRPCRequest`
    :returns: Returns basic information about the bot in form of a User object.
    :rtype: User
    """
    return TelegramBotRPCRequest('getMe', on_result=User.from_result, **kwargs)


# Token Constants

bot = TelegramBot('125579945:AAGjgsLLGeSqSILvfky71QjuMcZpeIBpuho')
#bot.update_bot_info().wait()
#print(bot.username)


json_file = 'data.json'
json_data = open(json_file)
data = json.load(json_data)
json_data.close()

#print data['result'][0]['message']['text']

# Renaming the JSON objects as string variables so that I don't have to
# type "data['x'][0]['y']['z']" all the time:


#text = data['result'][0]['message']['text']
#message_id = data['result'][0]['message']['message_id']
#chat_id = data['result'][0]['message']['chat']['id']


QuestionsList = [
'Does Cersei love her children?',
'Is the Hound really dead?',
'Is Jon Snow really dead?',
'Who killed Ygritte?',
'Why does Arya go blind?',
'Who is the prettiest girl in the show?',
'What promise did Lyanna force Ned to make before her death?',
'Who thought himself to be the prince who was promised?',
'Which prominent noble family currently seems to have a lot of wargs?',
'Where do the dragon eggs originate from?',
'Who is the man Bran meets at the end of the season 4, seemingly living under a weirwood tree?',
'What do the weirwood trees represent?',
'Who orchestrated the murder of Jon Arryn?',
'Who killed Joffrey?',
'Why did Jaime tell Tyrion that caused him to kill Tywin?',
'What species were the first humanoid creatures to walk on Westeros?',
'Which famous man bought down almost all Westeros to heel?'
]

arrayEnd = len(QuestionsList) - 1

i = random.randint(0, arrayEnd)


user_id = int(########)
last_update_id = 0 #last processed command


bot.send_message(user_id, 'Hello, please use the /question command to start the trivia!').wait()


'''while True:
    updates = bot.get_updates(offset = last_update_id + 1, limit = None, timeout=None).wait()
    

    r = requests.get('https://api.telegram.org/bot125579945:AAGjgsLLGeSqSILvfky71QjuMcZpeIBpuho/getUpdates')
    if r.status_code == 200:

        if not updates:
            continue

        else:
            #len(responses) - 1
            update_id = updates[0][0]
            last_update_id = update_id + 1

        for i in range(len(updates)): # probably range(len(updates[0][0]))

            # Process commands: 
            message = updates[i][1]
            chat_id = updates[i][1][3][0]
            username = updates[i][1][1][3]
            text = updates[i][1][7]

            print text

            i = i + 1


            if '/question' in text:
                bot.send_message(user_id, QuestionsList[i]).wait()'''
                


updates = bot.get_updates(offset=None,limit=2,timeout=None).wait()

for update in updates:
    gaga = updates[0][0]
    print(gaga)
