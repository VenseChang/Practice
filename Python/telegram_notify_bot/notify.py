import time
import sqlite3
import telepot
from pprint import pprint
from datetime import datetime
from telepot.loop import MessageLoop
from data import TOKEN


def start(msg):
    chat_id = msg['chat']['id']
    msg  = 'Welcome for use telegram notify bot.\n'
    msg += 'You can use this bot to remember everything, and you can set a time to push a notify for you.\n\n'
    msg += '/start\n=> get bot infomation.\n\n'
    msg += '/setNotify time things\n=> to set the msg and the notify time\n=> Time \' format ： yyyy-MM-dd HH:mm\n=> Example ： /setNotify 2017-08-27 12:00 have lunch'
    bot.sendMessage(chat_id, msg)


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
        insert = "INSERT INTO user('user_id', 'user_name', 'chat_id', 'msg', 'notify_time' ) VALUES ('{}', '{}', '{}', '{}', '{}')".format(user_id, user_name, chat_id, msg, notify_time)
        cursor.execute(insert)
        conn.commit()
        cursor.close()
        conn.close()
        bot.sendMessage(chat_id, 'Your notify setting already record.')
    except ValueError:
        bot.sendMessage(chat_id, 'Command\'format is Error.')



def on_chat_message(jsons):
    msg  = jsons['text']

    {
        '/start':start,
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
        bot.sendMessage(v[1], 'time\'up\n{}'.format(v[2]))
        cursor.execute('delete from user where user_no = ?;',(v[0],))
        conn.commit()
    cursor.close()
    conn.close()
    time.sleep(30)