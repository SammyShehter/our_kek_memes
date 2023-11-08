import os
import json
import random
import asyncio
from dotenv import load_dotenv
from utils import sendMessage, get_answer
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from datetime import datetime
from threading import Thread

load_dotenv()

dev = True if os.getenv("ENV") == "dev" else False

botToken = os.getenv(
    "MEMES_BOT_DEV") if dev else os.getenv("MEMES_BOT")

chat_ids = {os.getenv("SAMMY"): "Sammy",
            os.getenv("MAKHNADA"): "Makhnada",
            os.getenv("GARKAVAY"): "Garkavay"
            }

group_chat_id = os.getenv(
    "MEME_CHAT_DEV") if dev else os.getenv("MEME_CHAT")


class Bot:
    def __init__(self, token, chat_ids, polling_tasks_thread):
        self.application = ApplicationBuilder().token(token).build()
        self.CHANNEL_ID = os.getenv("MEME_CHANNEL_DEV") if dev else os.getenv("MEME_CHANNEL")
        self.CHECK_INTERVAL = 60
        self.last_member_count = 0
        self.fetching = False
        self.posting = False
        self.polling = True
        self.polling_tasks_thread = polling_tasks_thread
        self.chat_ids = {}
        try:
            for id, name in chat_ids.items():
                if id is not None:
                    int_id = int(id)
                    self.chat_ids[int_id] = name
                else:
                    raise ValueError(f"provided id for {name} is incorrect")
        except Exception as e:
            knownError = chat_ids.get(None)
            if knownError:
                sendMessage(
                    f"Error: {e}\nID is not configured for: {knownError}\nID's: {chat_ids}")
            else:
                sendMessage(f"Error: {e}\nID's: {chat_ids}")

    async def _run_scrap(self, sender):
        self.fetching = True
        process = await asyncio.create_subprocess_shell('python3 scrap.py')
        await process.wait()
        if sender != "Bot":
            for id, _ in self.chat_ids.items():
                await self.application.bot.send_message(chat_id=id, text=f"Done fetching started by {sender}... {datetime.now().strftime('%d.%m.%Y at %H:%M')}")
        self.fetching = False

    async def _post(self, sender):
        self.posting = True
        with open('./check.txt', 'r') as check_file:
            check = check_file.read().strip().split('\n')

        json_files = [file for file in os.listdir(
            './archive/') if file not in check]

        for file_name in json_files:
            with open(os.path.join('./archive/', file_name), 'r') as json_file:
                data = json.load(json_file)
                for entry in data:
                    await asyncio.sleep(random.randint(10, 45))
                    try:
                        if '.mp4?token' in data[entry]['src']:
                            await self.application.bot.send_video(chat_id=self.CHANNEL_ID, video=data[entry]['src'], disable_notification=True)
                        else:
                            await self.application.bot.send_photo(chat_id=self.CHANNEL_ID, photo=data[entry]['src'], disable_notification=True)
                    except Exception as e:
                        sendMessage(
                            f"main._post: {e} at {datetime.now().strftime('%d.%m.%Y at %H:%M')}")
                check.append(file_name)
                with open('./check.txt', 'w') as check_file:
                    check_file.write('\n'.join(check))
        if sender != "Bot":
            for id, _ in self.chat_ids.items():
                await self.application.bot.send_message(chat_id=id, text=f"Done with posting by {sender}... Back to idle mode")
        self.posting = False

    async def polling_tasks(self):
        while True:
            if self.polling:
                if not self.fetching:
                    await self._run_scrap("Bot")
                if not self.posting:
                    await self._post("Bot")
            await asyncio.sleep(3600)

    async def startHandler(self, update: Update, _: ContextTypes.DEFAULT_TYPE, context: ContextTypes.DEFAULT_TYPE):
        if update.message.chat.id not in self.chat_ids:
            return
        await context.bot.sendMessage(chat_id=update.message.chat.id, text="I'm a bot, please talk to me!")

    async def postHandler(self, update: Update, _: ContextTypes.DEFAULT_TYPE):
        if update.message.chat.id not in self.chat_ids:
            return
        if not self.posting:
            asyncio.create_task(self._post(
                self.chat_ids[update.message.chat.id]))
        else:
            await self.application.bot.send_message(chat_id=update.message.chat.id, text="Please wait for the previous posting task to finish")

    async def fetchMemesHandler(self, update: Update, _: ContextTypes.DEFAULT_TYPE):
        if update.message.chat.id not in self.chat_ids:
            return
        if not self.fetching:
            name = self.chat_ids[update.message.chat.id]
            asyncio.create_task(self._run_scrap(
                self.chat_ids[update.message.chat.id]))
            for id, _ in self.chat_ids.items():
                await self.application.bot.send_message(chat_id=id, text=f"Start fetching by {name}... {datetime.now().strftime('%d.%m.%Y at %H:%M')}")
        else:
            await self.application.bot.send_message(chat_id=update.message.chat.id, text="Please wait for the previous fetching task to finish")

    async def healthCheckHandler(self, update: Update, _: ContextTypes.DEFAULT_TYPE):
        if update.message.chat.id not in self.chat_ids:
            return
        await self.application.bot.send_message(chat_id=update.message.chat.id, text=f"Healthy {datetime.now().strftime('%d.%m.%Y at %H:%M')}")

    async def switchHandler(self, update: Update, _: ContextTypes.DEFAULT_TYPE):
        if update.message.chat.id not in self.chat_ids:
            return
        self.polling = not self.polling
        await self.application.bot.send_message(chat_id=update.message.chat.id, text=f"Click! Current switch position is set to {self.polling}")

    async def log(self, update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
        print(update)
        # if update.message.chat.id == group_chat_id:
        user_id = update.message.from_user.id
        user_name = update.message.from_user.username or ''
        first_name = update.message.from_user.first_name or ''

        text = update.message.text
        user = f"{('Username: ' + user_name + ' ') if user_name else ''}" \
            f"{('FirstName: ' + first_name + ' ') if first_name else ''}" \
            f"UserID: {user_id}"
        with open("user_logs.txt", "a") as f:
            f.write(f"{user}: {text}\n")
        words = text.split()
        number_of_words = len(words)
        gpt_response = 'ok'

        if number_of_words < 2:
            return
        gpt_response = get_answer(user, text)

        if gpt_response.lower() != 'ok' and gpt_response.lower() != 'ок' and gpt_response.lower() != 'ок.' and gpt_response.lower() != 'ok.':
            # await asyncio.sleep(random.randint(10, 45))
            await update.message.reply_text(text = gpt_response, reply_to_message_id = update.message.message_id)

if __name__ == '__main__':
    def start_polling_tasks():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(bot.polling_tasks())

    bot = Bot(botToken, chat_ids, Thread(target=start_polling_tasks))

    handlers = [
        MessageHandler(filters.TEXT & ~filters.COMMAND, bot.log),
        CommandHandler('start', bot.startHandler),
        CommandHandler('post', bot.postHandler),
        CommandHandler('fetch', bot.fetchMemesHandler),
        CommandHandler('check', bot.healthCheckHandler),
        CommandHandler('click', bot.switchHandler),
    ]

    for handler in handlers:
        bot.application.add_handler(handler)

    bot.polling_tasks_thread.start()
    print('Bot running')
    bot.application.run_polling()
