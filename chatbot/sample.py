from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)  # nombre del modulo o el paquete
spa_bot = ChatBot(
    "Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(spa_bot)
trainer.train("datos/datos.yml")
trainer.train("chatterbot.corpus.spanish")

@app.route('/')
def index():
    return render_template("index.html")  # ENVIAR A HTML


@app.route('/get')
def get_bot_response():
    # tomar datos de la entrada, escribimos js en el index.html
    userText = request.args.get("msg")
    return str(spa_bot.get_response(userText))


if __name__ == "__main__":
    app.run(debug=True)
