import os
import json
import random
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from datetime import datetime
from threading import Thread


class Bot:
    def __init__(self, token, chat_id, polling_tasks_thread):
        self.application = ApplicationBuilder().token(token).build()
        self.chat_id = chat_id
        self.fetching = False
        self.posting = False
        self.polling = True
        self.polling_tasks_thread = polling_tasks_thread

    async def _run_scrap(self):
        self.fetching = True
        process = await asyncio.create_subprocess_shell('python3 scrap.py')
        await process.wait()
        # await self.application.bot.send_message(chat_id=self.chat_id, text=f"Done fetching... {datetime.now().strftime('%d.%m.%Y at %H:%M')}")
        self.fetching = False

    async def _post(self):
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
                        if '.mp4?token' in data[entry]:
                            await self.application.bot.send_video(chat_id="@our_kek_memes", video=data[entry])
                        else:
                            await self.application.bot.send_photo(chat_id="@our_kek_memes", photo=data[entry])
                    except Exception as e:
                        print(
                            f"{e} {datetime.now().strftime('%d.%m.%Y at %H:%M')}")
                # await self.application.bot.send_message(chat_id=self.chat_id, text=f"{file_name} done, working on next file")
                check.append(file_name)
                with open('./check.txt', 'w') as check_file:
                    check_file.write('\n'.join(check))
        # await self.application.bot.send_message(chat_id=self.chat_id, text="Done with posting... Back to idle mode")
        self.posting = False

    async def polling_tasks(self):
        while True:
            if self.polling:
                if not self.fetching:
                    await self._run_scrap()
                if not self.posting:
                    await self._post()
            await asyncio.sleep(3600)

    async def startHandler(self, update: Update, _: ContextTypes.DEFAULT_TYPE, context: ContextTypes.DEFAULT_TYPE):
        if update.message.chat.id != self.chat_id:
            return
        await context.bot.sendMessage(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

    async def postHandler(self, update: Update, _: ContextTypes.DEFAULT_TYPE):
        if update.message.chat.id != self.chat_id:
            return
        if not self.posting:
            asyncio.create_task(self._post())
        else:
            await self.application.bot.send_message(chat_id=self.chat_id, text="Please wait for the previous posting task to finish")

    async def fetchMemesHandler(self, update: Update, _: ContextTypes.DEFAULT_TYPE):
        if update.message.chat.id != self.chat_id:
            return
        if not self.fetching:
            asyncio.create_task(self._run_scrap())
            # await self.application.bot.send_message(chat_id=self.chat_id, text=f"Start fetching... {datetime.now().strftime('%d.%m.%Y at %H:%M')}")
        else:
            await self.application.bot.send_message(chat_id=self.chat_id, text="Please wait for the previous fetching task to finish")

    async def healthCheckHandler(self, update: Update, _: ContextTypes.DEFAULT_TYPE):
        if update.message.chat.id != self.chat_id:
            return
        await self.application.bot.send_message(chat_id=self.chat_id, text=f"Healthy {datetime.now().strftime('%d.%m.%Y at %H:%M')}")

    async def switchHandler(self, update: Update, _: ContextTypes.DEFAULT_TYPE):
        if update.message.chat.id != self.chat_id:
            return
        self.polling = not self.polling
        if self.polling and (not hasattr(self, 'polling_tasks_thread') or not self.polling_tasks_thread.is_alive()):
            self.polling_tasks_thread = Thread(target=start_polling_tasks)
            self.polling_tasks_thread.start()
        await self.application.bot.send_message(chat_id=self.chat_id, text=f"Click! Current switch position is set to {self.polling}")



if __name__ == '__main__':
    def start_polling_tasks():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(bot.polling_tasks())

    bot = Bot('your-token', 'your-chat_id', Thread(target=start_polling_tasks))

    handlers = [
        CommandHandler('start', bot.startHandler),
        CommandHandler('post', bot.postHandler),
        CommandHandler('fetch', bot.fetchMemesHandler),
        CommandHandler('check', bot.healthCheckHandler),
        CommandHandler('click', bot.switchHandler),
    ]

    for handler in handlers:
        bot.application.add_handler(handler)

    bot.polling_tasks_thread.start()
    bot.application.run_polling()