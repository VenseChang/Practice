import time
import sqlite3
import telepot
from pprint import pprint
from datetime import datetime
from telepot.loop import MessageLoop
from data import NOTIFY_BOT_TOKEN as TOKEN

INDENTATION = '\t\t\t\t'

COMMAND  = '/start\n{}=> get bot infomation.\n\n'.format(INDENTATION)
COMMAND += '/help\n{}=> get command info.\n\n'.format(INDENTATION)
COMMAND += '/setNotify time things\n{}=> Time\'s format ： yyyy-MM-dd HH:mm\n{}=> Example ： /setNotify 2017-08-27 12:00 have lunch\n\n'.format(INDENTATION, INDENTATION)
COMMAND += '/get\n{}=> get all notify message in the conversation'.format(INDENTATION)
def start(msg):
    chat_id = msg['chat']['id']
    out  = 'Welcome for use telegram notify bot.\n'
    out += 'You can use this bot to remember everything, and you can set a time to push a notify for you.\n\n'
    out += COMMAND+'\n\n'
    bot.sendMessage(chat_id, out)


def set_notify(msgs):
    # get msg info
    chat_id = msgs['chat']['id']
    user_id = msgs['from']['id']
    user_name = msgs['from']['first_name']
    msg_split_ary = msgs['text'].split(' ')
    if len(msg_split_ary)<4:
        bot.sendMessage(chat_id, 'Syntax Error.')
    else:
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
            bot.sendMessage(chat_id, 'Syntax Error.')


def get_help(msg):
    chat_id = msg['chat']['id']
    bot.sendMessage(chat_id, COMMAND)


def get_info(msg):
    chat_id = msg['chat']['id']
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('select user_name,msg,notify_time from user where chat_id = ? order by notify_time asc', (chat_id,))
    values = cursor.fetchall()
    out=''
    if len(values)>0:
        out += '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=\n'
        for index, value in enumerate(values):
            out += 'user name  : {}\n'.format(value[0])
            out += 'message     : {}\n'.format(value[1])
            out += 'notify time : {}'.format(value[2])
            if index!=len(values):
                out += '\n'
            out += '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=\n'
    else:
        out = 'Here isn\'t any record in the conversation.'
    cursor.close()
    conn.close()
    bot.sendMessage(chat_id, out)

def on_chat_message(jsons):
    msg  = jsons['text']

    {
        '/start':start,
        '/help':get_help,
        '/setNotify':set_notify,
        '/get':get_info,
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