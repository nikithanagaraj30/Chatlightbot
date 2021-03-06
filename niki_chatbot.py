import logging 
import os 

from Adafruit_IO  import Data
YOUR_AIO_USERNAME = os.getenv('YOUR_AIO_USERNAME')  #ADAFRUIT_IO_USERNAME
YOUR_AIO_KEY = os.getenv('YOUR_AIO_KEY') #ADAFRUIT_IO_KEY
from Adafruit_IO import Client, Feed
aio = Client(YOUR_AIO_USERNAME,YOUR_AIO_KEY) 
  
#create feed
new= Feed(name='chatbot1') 
result= aio.create_feed(new) 

#logging exception handler
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

from telegram.ext import Updater, CommandHandler,MessageHandler, Filters 
import requests #Getting the data from the cloud
    
def ledoff(bot,update):
    value = Data(value=0) #Sending a value to a feed
    value_send = aio.create_data('chatbot1',value)
    chat_id = bot.message.chat_id
    update.bot.sendPhoto(chat_id=chat_id, photo="https://tse3.mm.bing.net/th?id=OIP.dTmDdvOWEO-0s7t0Z3Yr4gHaJ4&pid=Api&P=0&w=300&h=300", caption= "light off")
    
def ledon(bot,update):
    value = Data(value=1)
    value_send = aio.create_data('chatbot1',value)
    chat_id = bot.message.chat_id
    update.bot.sendPhoto(chat_id=chat_id, photo="https://tse1.mm.bing.net/th?id=OIP.E0jSIrVy0lS6LIULac0rngHaKj&pid=Api&P=0&w=300&h=300", caption="light on")
    
def echo(bot, update):
    #Echo the user message
    bot.message.reply_text(bot.message.text)

def main():
  BOT_TOKEN= os.getenv("BOT_TOKEN")
  u = Updater(BOT_TOKEN, use_context=True)
  dp = u.dispatcher
  dp.add_handler(CommandHandler("ledoff",ledoff))
  dp.add_handler(CommandHandler("ledon",ledon))
  dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
  u.start_polling()
  u.idle()
 
if __name__ == '__main__':
    main()
