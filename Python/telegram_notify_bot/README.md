# Telegram Bot - Notify bot

> can use this bot to record anything, and the bot will push message to user from the time which you set.

## Updating Diary
- 2017-08-27
    > add new command /clear
- 2017-08-26
    > add new command /help,/get

## Use
1. python  
2. sqlite3
3. [pip](requirements.txt)

## Command
### /start
> Get info from the bot
### /help
> Get command info
### /setNotify time things
> Time's format:yyyy-MM-dd HH:mm  
> Example：/setNotify 2017-08-27 12:00 favorite TV show
### /get
> Get all notify message in the conversation
### /clear
> Clear the notify message which the user who inserted in the conversation.

## Table schema
```sql
    CREATE TABLE `user` (
        `user_no` INTEGER PRIMARY KEY AUTOINCREMENT,
        `user_id` INTEGER NOT NULL, 
        `user_name` VARCHAR(30) NOT NULL, 
        `chat_id` INTEGER NOT NULL, 
        `msg` TEXT NOT NULL, 
        `notify_time` datetime NOT NULL 
    )
```