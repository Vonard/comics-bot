import telegram
import os
import random
from dotenv import load_dotenv
from comics import download_comic, check_comics

def main():
    load_dotenv()
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
    chat_id = os.environ['TG_CHAT_ID']
    random_comic = random.randint(1,check_comics())
    download_comic(random_comic)
    try:
        with open(f'{random_comic}.png', 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)
    finally:
        os.remove(f'{random_comic}.png')


if __name__ == "__main__":
    main()