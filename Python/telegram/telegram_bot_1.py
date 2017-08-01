import sys
import time
import telepot
from data import TOKEN
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

def on_chat_message(msg):
    _, _, chat_id = telepot.glance(msg)
    bot.sendMessage(chat_id, '汪汪汪') 


bot = telepot.Bot(TOKEN)
MessageLoop(bot, {
    'chat': on_chat_message,
}).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)