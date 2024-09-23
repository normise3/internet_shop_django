import threading
import os
from django.core.management import execute_from_command_line

from Market.telegram_bot import run_bot


def run_django():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    execute_from_command_line(['manage.py', 'runserver'])


# Создание и запуск потоков
if __name__ == '__main__':
    django_thread = threading.Thread(target=run_django)
    bot_thread = threading.Thread(target=run_bot)

    django_thread.start()
    bot_thread.start()

    django_thread.join()
    bot_thread.join()
