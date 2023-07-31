import telebot
import db_methods
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")



@bot.message_handler(regexp='set \d+')
def set_balance(message):
    balance_amt = float(message.text.split(' ', 1)[1])

    db_methods.insert_data(db_methods.conn, balance_amt, user_id=message.from_user.id)
    bot.reply_to(message, f"Баланс {balance_amt} успешно установлен") #добавить селект из бд и проверку, что баланс установлен корректно


#Подумать о том как вводить баланс впервый раз
@bot.message_handler(regexp='[-+]\d+')
def calc(message):
    user_id = message.from_user.id
    balance_amt = db_methods.select_balance(db_methods.conn, user_id)

    if ' ' in message.text:
        transaction_amt, transaction_desc = message.text.split(' ', 1)
    else:
        transaction_amt = message.text
        transaction_desc = "NULL"

    transaction_amt = transaction_amt.replace(',', '.')
    balance_amt += float(transaction_amt)
    
    db_methods.insert_data(db_methods.conn, balance_amt, user_id, transaction_amt, transaction_desc)
    bot.reply_to(message, f"<b>{message.from_user.first_name}</b> Остаток: {balance_amt}", parse_mode='HTML')


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()