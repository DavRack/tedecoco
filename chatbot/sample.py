from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import logging 
logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)

app = Flask(__name__)  # nombre del modulo o el paquete
spa_bot = ChatBot(
    "Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ListTrainer(spa_bot)
Banco = ["Lo siento, pero mi conocimiento no puede responder a esa pregunta :C",
         "hola",
         """QUEREMOS UN 5 EN ESTE TRABAJO <br>
................⢀⣤⣀⣀⣀⠀⠻⣷⣄             <br>
.........⢀⣴⣿⣿⣿⡿⠋⠀⠀⠹⣿⣦⡀ ⠀⠀      <br>
.⢀⣴⣿⣿⣿⣿⣏⠀⠀⠀⠀⠀⠀ ⢹⣿⣧ ⠀⠀      <br>
.⠙⢿⣿⡿⠋⠻⣿⣿⣦⡀⠀⠀⠀ ⢸⣿⣿⡆ ⠀⠀⠀⠀⠀<br>
......................⠈⠻⣿⣿⣦⡀⠀ ⢸⣿⣿⡇ ⠀⠀⠀ ⠀ <br>
...............................⠈⠻⣿⣿⣶⣿⣿⣿⠁ ⠀⠀   ⠀<br>
...........⣠⣿⣿⢿⣿⣶⣶⣶⣶⣾⣿⣿⣿⣿⡁        <br>
⢠⣶⣿⣿⠋⠀⠀⠉⠛⠿⠿⠿⠿⠿⠛⠻⣿⣿⣦⡀    <br>
⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠈⠻⣿⡿""",
    "Quien es tu padre?",
    """Isabela Luján Jaramillo, <br>  
Salome Aristizabal Giraldo,  <br>
Ricardo José Garzón Arias,   <br>
Mauricio Zapata Pereira, <br>
Ana La Princesa Guerrera, <br>
Juan Pablo Ciro Londoño, <br>
David Londoño Montoya.""",
"Que hace la aplicación?",
"Nuestra aplicacion es una herramienta CASE (Computer Aided Software Engineering) que genere un aplicativo funcional a partir de un modelo de procesos BPMN, El Cual fue propuesto por el docente Fernan Alonso Villa Garzon :D.",
"Donde Genero el BPMN?",
"https://demo.bpmn.io/new",
"Cuales son las reglas?",
"""NOTAS DE CONSISTENCIA O REGLAS:<br>
1) NO SE PERMITE ANIDAR VENTANAS ENTRE SI, <br>
2) NO SE PERMITEN INSERTAR IMAGENES EN LA APLICACION,<br>
3) SI VA HACER UN FORMULARIO SOLO SE PUEDE HACERLO EN UN LANE,<br>
4) SOLO SE PUEDE HACER UN FORMULARIO POR VENTANA,<br>
5) NO SE PUEDEN DEJAR LANES VACIOS,<br>
6) EL DIAGRAMA SE DEBE REALIZAR EN EL ORDEN QUE DESEA QUE SE MUESTRE,<br>
7) SI VA A MODIFICAR EL DIAGRAMA DEBE HACERLO DESDE EL CÓDIGO XML O REHACER LAS CONEXIONES ENTRE LAS PARTES DEL DIAGRAMA PARA EVITAR ERRORES EN LA VISTA,<br>
8) TODOS LOS TEXTBOX Y RADIOBUTTON SE DEBEN ALMACENAR, POR ENDE, TODOS DEBEN TENER UNA CONEXIÓN CON EL SIMBOLO DE STORAGE,<br>
9) NO SE DEBE REPETIR EL NOMBRE DEL SIMBOLO DE STORAGE.""",
"Significado de simbolos",
"""textAnnotation (un comentario) -> contenido de una tarea<br>
participant(un participant)-> es una ventana <br>
task (una tarea) -> dibujar en pantalla un elemento(que su nombre lo define) y el nombre de ese elemento(definido por el comentario)<br>
sequenceFlow -> una conexion entre dos o más objetos<br>
exclusiveGateway (un rombo) -> es un if <br>
lane (linea) -> un div en html(incluyendo su contenido)<br>
DataStoreReference (Storage Symbol) -> el nombre del simbolo será el id del elemento al que está conectado en el html""",
"Que lenguaje se implemento?",
"Python,HTML,CSS y BPMN",
"¿Dónde se almacenan los datos?",
"En un lindo archivo de texto en una linda carpeta del proyecto llamada files :3"
]
trainer.train(Banco)
#trainer.train("chatterbot.corpus.spanish")

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
