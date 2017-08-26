# Telegram Bot - Notify bot

> can use this bot to record anything, and the bot will push message to user from the time which you set.

## Use
1. python  
2. sqlite3

## Command
### /start
> get info from the bot
### /setNotify time things
> Time's format:yyyy-MM-dd HH:mm  
> Example：/setNotify 2017-08-27 12:00 favorite TV show

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