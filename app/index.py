from flask import Flask, render_template


class Button:
    def __init__(self, id, title, style):
        self.id = id
        self.title = title
        self.style = style

    def getHtml(self):
        return '<button class="{0}">{1}</button>'.format(self.style, self.title)

class Dropdown:
    def __init__(self, id, title, items):
        self.id = id
        self.title = title
        self.items = items

    def getHtml(self):
        lista = ""
        c = 0
        for i in self.items:
            lista += '<option value="{0}">{1}</option>'.format(c, i)
            c+=1

        return '''
            <select class="custom-select my-2 col-12 mx-auto">
                <option selected>{0}</option>
                {1}
            </select>'''.format(self.title, lista)

class DivTitle:
    def __init__(self, title, style):
        self.title = title
        self.style = style

    def getHtml(self):
        return '<div class="{0}">{1}</div>'.format(self.style, self.title)

app = Flask(__name__)


@app.route('/')
def home():

    # Static content
    title = "Pizzas napoles"
    navbar = '''
        <nav class="navbar navbar-expand-md nav-background">
            <div class="container"> 
                <a class="navbar-brand mx-auto k-font" href="/">Napoles</a> 
            </div>
        </nav>
    '''

    # XML testing examples (this will be removed)
    pizzas = Dropdown(0, "Change pizza", ["jawayana", "shiampiñones", "Musho keso", "zalami"])
    doOrder = Button(1, "Hacer pedido", "btn btn-custom mx-auto k-font")
    selectPizza = DivTitle("Por favor seleccione una picsa:" , "mx-auto h1 k-font")

    items = [selectPizza, pizzas, doOrder]

    contenido = ""
    for item in items:
        contenido += item.getHtml() + '\n'

    return render_template("home.html", title=title, nav=navbar, page=contenido)


if __name__ == "__main__":
    app.run(debug=True)
