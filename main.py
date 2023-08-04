import os
import json
import time
import random
import asyncio
#import threading
#import subprocess
# import warnings
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from datetime import datetime

# warnings.filterwarnings("ignore", category=RuntimeWarning)
application = ApplicationBuilder().token('6190741084:AAEKoD9nZjWVL6haVmqm-WO3zwsd6jRmLEs').build()
polling = False

#def scrap_process():
#    process = subprocess.Popen(['python3', 'scrap.py'])
#    process.wait()

#async def endlessKek():
#    while polling:
#        scrap_process()
#        time.sleep(1000)
#        await post()
async def run_other_script():
    process = await asyncio.create_subprocess_shell('python3 scrap.py')
    await process.wait()
    await application.bot.send_message(chat_id=705606971, text=f"Done fetching... {datetime.now().strftime('%d.%m.%Y at %H:%M')}")

async def post():
    with open('./check.txt', 'r') as check_file:
        check = check_file.read().strip().split('\n')

    json_files = [file for file in os.listdir('./archive/') if file not in check]

    for file_name in json_files:
        with open(os.path.join('./archive/', file_name), 'r') as json_file:
            data = json.load(json_file)
            for entry in data:
                time.sleep(random.randint(10, 45))
                try:
                    await application.bot.send_photo(chat_id="@our_kek_memes", photo=data[entry])
                except Exception as e:
                    print(f"{e} {datetime.now().strftime('%d.%m.%Y at %H:%M')}")
            await application.bot.send_message(chat_id=705606971, text=f"{file_name} done, working on next file")
            check.append(file_name)
            with open('./check.txt', 'w') as check_file:
                check_file.write('\n'.join(check))
    await application.bot.send_message(chat_id=705606971, text="Done with posting... Back to idle mode")

async def startHandler(update: Update, _: ContextTypes.DEFAULT_TYPE, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.id != 705606971:
        return
    await context.bot.sendMessage(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def postHandler(update: Update, _: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.id != 705606971:
        return
    await post()
    
async def fetchMemesHandler(update: Update, _: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.id != 705606971:
        return
    asyncio.create_task(run_other_script())
    await application.bot.send_message(chat_id=705606971, text=f"Start fetching... {datetime.now().strftime('%d.%m.%Y at %H:%M')}")

async def healthCheckHandler(update: Update, _: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.id != 705606971:
        return
    await application.bot.send_message(chat_id=705606971, text=f"Healthy {datetime.now().strftime('%d.%m.%Y at %H:%M')}")
async def switchHandler(update: Update, _: ContextTypes.DEFAULT_TYPE):
    global polling
    if update.message.chat.id != 705606971:
        return
    polling = not polling
    await application.bot.send_message(chat_id=705606971, text=f"Click! Current switch position is set to {polling}")
if __name__ == '__main__':
    # thread = threading.Thread(target=endlessKek)
#    thread = threading.Thread(target=lambda: asyncio.run(endlessKek()))
#    thread.start()
    
    startH = CommandHandler('start', startHandler)
    # echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    postH = CommandHandler('post', postHandler)
    fetchH = CommandHandler('fetch', fetchMemesHandler)
    healthH = CommandHandler('check', healthCheckHandler)
    switchH = CommandHandler('click', switchHandler)
    # inline_caps_handler = InlineQueryHandler(inline_caps)
    # unknown_handler = MessageHandler(filters.COMMAND, unknown)


    application.add_handler(startH)
    # application.add_handler(echo_handler)
    application.add_handler(postH)
    application.add_handler(fetchH)
    application.add_handler(healthH)
    application.add_handler(switchH)
    # application.add_handler(inline_caps_handler)
    # application.add_handler(unknown_handler)

    
    application.run_polling()
#    thread.join()

# User(can_join_groups=True, can_read_all_group_messages=False, first_name='Our Kek Memes Bot', id=6190741084, is_bot=True, supports_inline_queries=False, username='our_kek_memes_bot')

#Update(
# message=Message(
#   channel_chat_created=False,
#   chat=Chat(
#       first_name='Sammy',
#       id=705606971, 
#       last_name='Shehter', 
#       type=<ChatType.PRIVATE>,
#       username='SammyShehter'
#   ), 
#   date=datetime.datetime(2023, 7, 21, 10, 37, 56, tzinfo=datetime.timezone.utc),
#   delete_chat_photo=False,
#   entities=(
#       MessageEntity(
#           length=6,
#           offset=0,
#           type=<MessageEntityType.BOT_COMMAND>
#       ),
#   ),
#   from_user=User(
#       first_name='Sammy',
#       id=705606971,
#       is_bot=False,
#       language_code='en',
#       last_name='Shehter',
#       username='SammyShehter'
#   ),
#   group_chat_created=False,
#   message_id=1,
#   supergroup_chat_created=False,
#   text='/start'),
#   update_id=182770355)

#Update(
#   message=Message(
#       channel_chat_created=False,
#       chat=Chat(
#           id=-1001615864926,
#           title='Our Memes Chat',
#           type=<ChatType.SUPERGROUP>,
#           username='our_kek_memes_group'
#       ),
#       date=datetime.datetime(2023, 7, 21, 10, 38, 53, tzinfo=datetime.timezone.utc),
#       delete_chat_photo=False,
#       from_user=User(
#           first_name='Group',
#           id=1087968824,
#           is_bot=True,
#           username='GroupAnonymousBot'
#       ),
#       group_chat_created=False,
#       message_id=7,
#       sender_chat=Chat(
#           id=-1001615864926,
#           title='Our Memes Chat',
#           type=<ChatType.SUPERGROUP>,
#           username='our_kek_memes_group'
#       ),
#       supergroup_chat_created=False,
#       text='test1'
#   ),
#   update_id=182770356
# )
# )
