# Публикация комиксов

С помощью данного проекта вы можете скачивать случайный комикс с сайта [xkcd.com](https://xkcd.com/) и отправлять его на свой телеграм канал.

### Как установить

Что бы работать с ботом, создайте .env файл в папке проекта и запишите туда:
```
TELEGRAM_BOT_TOKEN=Ваш токен
TG_CHAT_ID=id вашего чата
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Как запустить

Что бы запустить программу в командной строке перейдите в папку проекта и выполните команду:
```
python bot.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).