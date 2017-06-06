import telebot
from parsers import utils, dou_parser, ain_parser
import consts

bot = telebot.TeleBot(consts.BOT_TOKEN)


@bot.message_handler(commands=["start"])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row("ain.ua", "dou.ua")
    bot.send_message(chat_id=message.from_user.id,
                     text="Привет. Я могу показать тебе, что там новенького на "
                          "{0} или "
                          "{1}. "
                          "Выбери что-то одно:".format(utils.DOU_BASE_URL,
                                                       utils.AIN_BASE_URL),
                     parse_mode="Markdown",
                     reply_markup=user_markup,
                     disable_web_page_preview=True)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    cards = []
    if message.text == "dou.ua":
        cards = dou_parser.parse_postcards()
    elif message.text == "ain.ua":
        cards = ain_parser.parse_postcards()

    if cards:
        resp = [card.link for card in cards]

        [bot.send_message(message.from_user.id,
                          card,
                          parse_mode="Markdown") for card in resp]
    else:
        bot.send_message(chat_id=message.from_user.id, text="Что-то пошло не так")


@bot.message_handler(content_types=["command"])
def handle_command(message):
    pass


bot.polling(none_stop=True, interval=0)
