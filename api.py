# Импортируем модули для работы с JSON и логами.
import json
import logging

# Импортируем подмодули Flask для запуска веб-сервиса.
from flask import Flask, request

app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)

# Хранилище данных о сессиях.
sessionStorage = {}

# Задаем параметры приложения Flask.
@app.route("/", methods=["POST"])
def main():
    # Функция получает тело запроса и возвращает ответ.
    logging.info("Request: %r", request.json)

    response = {
        "version": request.json["version"],
        "session": request.json["session"],
        "response": {"end_session": False},
    }

    handle_dialog(request.json, response)

    logging.info("Response: %r", response)

    return json.dumps(response, ensure_ascii=False, indent=2)


# Функция для непосредственной обработки диалога.
def handle_dialog(req, res):
    # user_id = req["session"]["user_id"]

    if req["session"]["new"]:
        # Это новый пользователь.
        # Инициализируем сессию и поприветствуем его.
        res["response"]["text"] = "Привет! Чем могу Вам помочь?"
        question = [{"title": "На кого я похож?", "hide": True}]
        res["response"]["buttons"] = question
        return

    # Обрабатываем ответ пользователя.
    if "похож" in req["request"]["original_utterance"].lower():
        res["response"][
            "text"
        ] = "На придурка, который разговаривает со своим телефоном"
        return

    # Если нет, то убеждаем его купить слона!
    res["response"]["text"] = "К такому меня не готовили. Повторите вопрос."
    res["response"]["buttons"] = question
