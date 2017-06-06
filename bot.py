import telebot
from parsers.parser import parse_postcards
import consts

bot = telebot.TeleBot(consts.BOT_TOKEN)


@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(chat_id=message.from_user.id,
                     text="Привет. Я могу показать тебе, что там новенького на [https://dou.ua](URL)."
                          " Если хочешь, ответь 'да'",
                     parse_mode="Markdown")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "да":
        cards = parse_postcards()
        resp = [card.link for card in cards]
        print(resp)
        [bot.send_message(message.from_user.id,
                          card,
                          parse_mode="Markdown") for card in resp]


@bot.message_handler(content_types=["command"])
def handle_command(message):
    pass


bot.polling(none_stop=True, interval=0)
