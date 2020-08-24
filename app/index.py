from flask import Flask, render_template


class Button:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def getHtml(self):
        return '<button class="btn btn-secondary">' + self.title + '</button>'


class Dropdown:
    def __init__(self, id, title, items):
        self.id = id
        self.title = title
        self.items = items

    def getHtml(self):
        lista = ""

        for i in self.items:
            lista += '<a class="dropdown-item" href="#">'+i+'</a>'

        return '''
            <div class="dropdown">
                <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    {0}
                    </button>
                <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    {1}
                </div>
            </div>'''.format(self.title, lista)


app = Flask(__name__)


@app.route('/')
def home():

    title = "Pizzas napoles"
    navbar = '''
        <nav class="navbar navbar-expand-md nav-background">
            <div class="container"> 
                <a class="navbar-brand mx-auto" href="/">Napoles</a> 
            </div>
        </nav>
    '''

    pizzas = Dropdown(2, "Change pizza", [
                      "jawayana", "shiampiñones", "Musho keso"])
    doOrder = Button(3, "Hacer pedido")

    items = [navbar,pizzas.getHtml(), doOrder.getHtml()]

    contenido = ""

    for item in items:
        contenido += item + '\n'

    return render_template("home.html", title=title, page=contenido)


if __name__ == "__main__":
    app.run(debug=True)