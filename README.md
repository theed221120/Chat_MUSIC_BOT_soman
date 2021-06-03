# CHAT MUSIC BOT SOMAN

### ![Music_for_hsk_bot ](https://telegra.ph/file/b68eb037b82f5312a5b4f.jpg)

**A [CallsMusic](https://github.com/callsmusic/callsmusic) Based Telegram Bot With Some Cool Extra Features ❤️**


## Note!⚠️ ,
_**You need another (dummy) Telegram Account To Use/Deploy This!**_

## Features 🔥️

- **Play Music In Telegram Group Voice Chats!** (Supports Multiple Groups)
- **Search For YouTube Videos Inline!**
- **Download Yt Songs By It's Name!** (Ex:- `/yts faded` )
- **Download Yt Videos By It's Name!** (Ex:- `/ytvid faded` )
- **Saavn Music Download**  (Ex:- `/saavn teri meri kahani` )
- **Deezer Music Download** (Ex:- `/deezer faded` )
- **Supports Queues!**
- **Get Voice Chat Link!** (`/vc` - Public Groups Only )
- **Get Lyrics Of Your Song!** (Ex:- `/lyrics faded` )
- **Join & Leave Streamer Account Using A Command** (To Join - `joingrp` , To Leave `leavegrp` )


# Deployment
Before You Deploy make sure you Starred & Forked **[The Original Repo ❤️](https://github.com/callsmusic/callsmusic)** . **And [This Repo!](https://github.com/theed221120/Chat_MUSIC_BOT_soman.git)** 🤗️


## The Easy Way ⚡️

### With Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/theed221120/Chat_MUSIC_BOT_soman.git)

### With Zeet
<a href="https://zeet.co/new/template/itz-fork/yeah-my-man"><img src="https://user-images.githubusercontent.com/77770753/119371372-fe917900-bcd3-11eb-8db5-f5e8063cdd1c.jpg" width="94" height="28"></a>


#### Get Pyrogram String Session
<a href="https://replit.com/@IamHirusha/GetPyroSessionVC"><img src="https://img.shields.io/badge/Run-Repl.it-white?style=for-the-badge&logo=repl.it"></a>


## Support!
Facing Problems While Deploying or Using? **[Read How To Deploy](https://github.com/theed221120/Chat_MUSIC_BOT_soman.git/wiki/How-To-Deploy-This!)**
or Ask Me In **[Nexa Bots Support Group](https://t.me/hsk_the_editor)**


### Config Vars 😂,

 `SESSION_NAME` - Your Pyrogram String Session!</br>
 `BOT_TOKEN` - Your Bot Token</br>
 `API_ID` - Your API ID</br>
 `API_HASH` - Your API HASH</br>
 `SUDO_USERS` - Sudo User's ID</br>
 `DURATION_LIMIT` - Max Time Limited For a song!</br>
 `USER_ACCNAME` - Your bot's streamer account username without "@" ! </br>
 `ARQ_API_KEY` - Your ARQ api key! Get your own at [ARQ Bot](https://t.me/ARQRobot)

**[How To Get Config Vars? 🤔 Read This!](https://github.com/Itz-fork/yeah-my-man/wiki/How-To-Deploy-This!)**


# The Hard Way!

## Deploy In Your PC (or whatever)

#### For Ubuntu Based OS

**First run this command** - ``` sudo apt update ```

- Install Python,
```
sudo apt install software-properties-common
```
```
sudo add-apt-repository ppa:deadsnakes/ppa
```
```
sudo apt install python3.9
```

- Install ffmpeg,
```
sudo apt install ffmpeg
```

- Install Git,
```
sudo apt install git
```

- Clone This Repo, 
```
git clone https://github.com/theed221120/Chat_MUSIC_BOT_soman.git
```

- Enter File Dir; 
```
cd Callsmusic-Plus
```

- Install Other Requirements, 
```
pip3 install -r requirements.txt
```

- Go to **config.py** and edit it this with **[your own values](https://github.com/Itz-fork/yeah-my-man/wiki/How-To-Deploy-This!)**

- Finally Let's run the bot, 
```
python3 main.py
```


**For guide on other OS check [This wiki page](https://github.com/Itz-fork/yeah-my-man/wiki/Install-On-Other-OS)**

### Requirements

- FFmpeg
- Python 3.7+

### Config

Copy `example.env` to `.env` and fill it with your credentials.


### Using Docker

1. Build:
   ```bash
   docker build -t musicplayer .
   ```
2. Run:
   ```bash
   docker run --env-file .env musicplayer
   ```


## Credits

- [CallsMusic](https://github.com/callsmusic/callsmusic) ~ This is the original Repo! ❤️
- **[Roj](https://github.com/rojserbest) & [Marvin](https://github.com/BlackStoneReborn)** : development
- **[Laky](https://github.com/Laky-64) & [Andrew](https://github.com/AndrewLaneX)** : PyTgCalls
- **Mr Dark prince**
- **TeamDaisyX**
- **N A C CREATIVE**: For Voice Chat Link Command!


## License

### GNU General Public License v3.0
[Read more](http://www.gnu.org/licenses/#GPL)
