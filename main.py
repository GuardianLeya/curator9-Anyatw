import telebot

bot = telebot.TeleBot('6472605186:AAGe4K1wqxqdJITZEsIQ3yRvCISyRrmdoAc')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Купи слона')


@bot.message_handler(commands=['no'])
def main(message):
    bot.send_message(message.chat.id, 'Ну купи слона')


@bot.message_handler(commands=['yes'])
def main(message):
    bot.send_message(message.chat.id, 'Все так говорят, а ты купи слона')


@bot.message_handler(commands=['exit'])
def main(message):
    bot.send_message(message.chat.id, 'Купи слона')


@bot.message_handler(commands=['end'])
def main(message):
    bot.send_message(message.chat.id, 'Купи слона')


@bot.message_handler(commands=['bye'])
def main(message):
    bot.send_message(message.chat.id, 'Ты думаешь, эти команды на что-то влияют? Купи слона')


bot.infinity_polling()
