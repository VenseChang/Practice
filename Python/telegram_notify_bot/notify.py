import time
import sqlite3
import telepot
from pprint import pprint
from datetime import datetime
from telepot.loop import MessageLoop
from data import NOTIFY_BOT_TOKEN as TOKEN

COMMAND  = '/start\n=> get bot infomation.\n\n'
COMMAND += '/setNotify time things\n=> Time \' format ： yyyy-MM-dd HH:mm\n=> Example ： /setNotify 2017-08-27 12:00 have lunch'

def start(msg):
    chat_id = msg['chat']['id']
    out  = 'Welcome for use telegram notify bot.\n'
    out += 'You can use this bot to remember everything, and you can set a time to push a notify for you.\n\n'
    out += COMMAND+'\n\n'
    out += '/help => get command infomation.'
    bot.sendMessage(chat_id, out)


def set_notify(msgs):
    # get msg info
    chat_id = msgs['chat']['id']
    user_id = msgs['from']['id']
    user_name = msgs['from']['first_name']
    msg_split_ary = msgs['text'].split(' ')
    try:
        notify_time = datetime.strptime(msg_split_ary[1] + ' ' + msg_split_ary[2] , '%Y-%m-%d %H:%M')
        msg = ''
        for t in msg_split_ary[3:]:
            msg += t + ' '

        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user('user_id', 'user_name', 'chat_id', 'msg', 'notify_time' ) VALUES (?, ?, ?, ?, ?)",(user_id, user_name, chat_id, msg, notify_time,))
        conn.commit()
        cursor.close()
        conn.close()
        bot.sendMessage(chat_id, 'Your notify setting already record.')
    except ValueError:
        bot.sendMessage(chat_id, 'Command\'format is Error.')


def get_help(msg):
    chat_id = msg['chat']['id']
    bot.sendMessage(chat_id, COMMAND)

def on_chat_message(jsons):
    msg  = jsons['text']

    {
        '/start':start,
        '/help':get_help,
        '/setNotify':set_notify,
    }[msg.split(' ')[0]](jsons)


bot = telepot.Bot(TOKEN)
MessageLoop(bot, {
                    'chat': on_chat_message
                  }).run_as_thread()

print('Listening ...')

while 1:
    times = datetime.now().strftime('%Y-%m-%d %H:%M')+'%'

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('select user_no,chat_id,msg from user where notify_time like ?', (times,))
    values = cursor.fetchall()
    for v in values:
        bot.sendMessage(v[1], 'Time which you set up is up\n{}'.format(v[2]))
        cursor.execute('delete from user where user_no = ?;',(v[0],))
        conn.commit()
    cursor.close()
    conn.close()
    time.sleep(30)