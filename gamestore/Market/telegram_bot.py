from telebot import TeleBot
import sys
import os
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gamestore.settings')

django.setup()

from models import Game

token = "7125954288:AAHuEUOPeZ_Ug_LnagHH6DSJqKxwidl_cA8"
bot = TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я ігровий бот. Введіть /buy_game, щоб купити гру, /popular, щоб "
                          "отримати список популярних ігор.")


@bot.message_handler(commands=['buy_game'])
def add_game(message):
    bot.reply_to(message, "Введіть назву гри:")
    bot.register_next_step_handler(message, process_game_name)


def process_game_name(message):
    try:
        game = Game.objects.get(name=message.text)
        bot.reply_to(message,
                     f"Бажаєте купити {game.name}? [Перейдіть на наш сайт]"
                     f"(http://127.0.0.1:8000/buy_game/{game.name}).", parse_mode='Markdown')
    except Game.DoesNotExist:
        bot.reply_to(message,
                     f"Вибачте, але гри {message.text} немає в наявності. Ви також можете переглянути наш "
                     f"каталог і вибрати іншу гру!")


@bot.message_handler(commands=['popular'])
def show_popular_games(message):
    games = Game.objects.order_by('?')[:6]
    if games:
        game_list = "\n".join([f"{i + 1}. {game.name}" for i, game in enumerate(games)])
        bot.reply_to(message, f"Ось шість популярних ігор, які ви можете переглянути:\n\n{game_list}")
    else:
        bot.reply_to(message, "На жаль, не вдалося знайти жодної гри.")


def run_bot():
    bot.remove_webhook()
    bot.polling(none_stop=True, interval=0)
