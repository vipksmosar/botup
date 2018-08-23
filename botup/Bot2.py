import apiai
import json
import socket
import socks
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#ipprox = "103.46.128.49"
#portprox = 26060
#socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, ipprox, portprox)
#socket.socket = socks.socksocket

updater = Updater(token="549557834:AAESyEgIiPFOA3gkEYcF9ihlpRBLs1Ucmys")
dispatcher = updater.dispatcher
print('ndo')


def startC(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Не пиши сюда!!!')
    print('nexer')


def textM(bot, update):
    response = '[r[r' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)
    print(response)

start_command_handler = CommandHandler('start', startC)
text_message_handler = MessageHandler(Filters.text, textM)
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
updater.start_polling(clean=True)
updater.idle()
