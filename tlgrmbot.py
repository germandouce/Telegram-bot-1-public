import time
import datetime
import telebot
import telegram_send
import random
import datos

bot_token = ''

bot = telebot.TeleBot(token = bot_token)

#Cry func
def llorar2(msj):
    """
    ARGS: msj is a str

    RETURNS: llorar is a bool in case of finding any word in dict 'datos'
    """
    llorar = False
    for queja in datos.quejas.values():
        if queja in msj and llorar == False:
            llorar = True
    return llorar

#random_question func
def random_question():
    question_list = list((datos.preguntas.items())) #Convert saludos to a list of iterables (tuples)
    random_question = random.choice(question_list)[1] #Choose a random entry from saludos_list (tuple[1])
    return random_question

#/start command handler
@bot.message_handler(commands=['start']) #I use a decorator
def send_welcome(message):
    saludos_list = list((datos.saludos.items())) #Convert saludos to a list of iterables (tuples)
    saludo_random = random.choice(saludos_list)[1] #Choose a random entry from saludos_list (tuple[1])
    bot.reply_to(message,saludo_random)

#/help command handler
@bot.message_handler(commands=['help']) #I use a decorator
def send_welcome(message):
    bot.reply_to(message,'Use the commands!')

#/@ig command handler
@bot.message_handler(commands=['ig_username']) #I use a decorator
def send_sendusername(message):
    texts = message.text.split()
    texts.pop(0)
    str=' '
    str=str.join(texts)
    bot.reply_to(message, 'https://instagram.com/{}'.format(str))

#/random_question command handler
@bot.message_handler(commands=['random_question'])
def send_question(message):
    bot.reply_to(message,random_question())

#cry listening handler
@bot.message_handler(func=lambda msj: msj.text is not None and llorar2(msj.text))
def at_cry (message):
    bot.reply_to(message, '\U0001F62D')

#telegram_send.send(messages=['No jodo mas'])

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15) 
