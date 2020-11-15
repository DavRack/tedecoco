from flask import Flask, render_template, request
import json
# import controllers.Firebase as fairbeis
import controllers.Parseo as Parce
from models.Button import Button
from models.DivTitle import DivTitle
from models.Dropdown import Dropdown
from models.Form import Form
from models.Input import Input
from models.Radio import Radio
from models.Tooltip import Tooltip as TP
import re
import os

navbar = ""
footer = '''
        <footer class="fixed-bottom k-font darkblue m-0">
            <div class= "container">
                <div class="row m-0 justify-content-center py-2 align-content-center">
                    <a class="mr-2"> <i class="fab fa-instagram fa-fw fa-2x"></i> </a>
                    <a> <i class="fab fa-facebook-square fa-fw fa-2x"></i> </a>
                    <a class="ml-2"> <i class="fab fa-linkedin fa-fw fa-2x"></i> </a>
                    <p class="p-0 m-0 text-right col-3 my-auto">Todos los derechos reservados <i class="far fa-copyright"></i></p>
                </div>
            </div>
        </footer>
    '''


class Navbar:
    def __init__(self, icon, title):
        self.icon = icon
        self.title = title

    def getHtml(self):
        return '''
        <nav class="navbar navbar-expand-md nav-background">
            <div class="container">
                <a class="navbar-brand mx-auto k-font" href="/"><i class="{0}"></i> {1}</a>
            </div>
        </nav>
        '''.format(self.icon, self.title)


app = Flask(__name__)


@app.route('/upload', methods=["POST"])
def upload():
    if request.method == "POST":
        if request.files:
            if(request.files['diagram'].filename != ""):
                xmlFile = request.files['diagram']

                title = xmlFile.filename

                if re.findall(r"\.{1}bpmn$", title):
                    # En esta área se interpreta el XML

                    dic = Parce.returnActivityElements(xmlFile)
                    items = []
                    ids = []
                    ids.append({"id": 0, "name": title})
                    contenido = ""

                    for d in dic:
                        aux = []
                        for i in dic[d]:

                            if ("Boton" in i[0]):
                                if (len(dic[d]) == 1):
                                    aux.append(
                                        Button(1, i[1], "btn btn-custom k-font"))
                                else:
                                    submitBtn = Button(
                                        1, i[1], "btn btn-custom k-font")

                            elif ("Textbox" in i[0]):
                                id = i[3][0]
                                
                                
                                ids.append(
                                    {"id": id, "name": i[1], "type": "text"})
                                aux.append(
                                    Input(id, "col-12 mb-3", "text", "form-control", '', i[1], id))
                            elif ("Radio" in i[0]):
                                id = i[3][0]
                                ids.append(
                                    {"id": id, "name": i[1], "type": "radio"})
                                aux.append(
                                    Radio(id, "col-12 mb-3", "radio", "form-control", '', i[1], id, i[1].split(" ")[0]))
                            elif ("Desplegable" in i[0]):
                                l = list(i[1].split(","))
                                aux.append(Dropdown(1, l[0], l))
                            elif ("Titulo" in i[0]):
                                aux.append(DivTitle(i[1], "mx-auto h1 k-font"))
                            elif ("Navbar" in i[0]):
                                navbar = (Navbar("fas fa-paw", i[1])).getHtml()
                            else:
                                print(3)
                        if (len(dic[d]) == 1):
                            for i in aux:
                                items.append(i)
                        else:
                            formu = Form("w-100 row m-0 justify-content-center", "/read",
                                         "POST", "multipart/form-data", aux, submitBtn, ".*")
                            items.append(formu)

                    for item in items:
                        contenido += item.getHtml() + '\n'

                    f = open("../tedecoco/app/files/names.txt", "w+")
                    f.writelines(json.dumps(ids))
                    f.close()

                    return render_template("home.html", title=title, nav=navbar, page=contenido, ids=ids, foot=footer)
                else:
                    title = "Error"

                    navbar = '''
                        <nav class="navbar navbar-expand-md nav-background">
                            <div class="container"> 
                                <a class="navbar-brand mx-auto k-font" href="/"><i class="fas fa-pizza-slice fa-fw"></i> Napoles</a> 
                            </div>
                        </nav>
                    '''

                    contenido = '''
                        <h1 class="text-center w-100 mb-3">El archivo no es un diagrama BPMN</h1>
                        <a class="btn btn-custom mx-auto" href="/">Ir atrás</a>
                    '''

                    return render_template("home.html", title=title, nav=navbar, page=contenido, foot=footer)
            else:
                title = "Error"

                navbar = '''
                    <nav class="navbar navbar-expand-md nav-background">
                        <div class="container"> 
                            <a class="navbar-brand mx-auto k-font" href="/"><i class="fas fa-pizza-slice fa-fw"></i> Napoles</a> 
                        </div>
                    </nav>
                '''

                contenido = '''
                    <h1 class="text-center w-100 mb-3">No se seleccionó diagrama</h1>
                    <a class="btn btn-custom mx-auto" href="/">Ir atrás</a>
                '''

                return render_template("home.html", title=title, nav=navbar, page=contenido, foot=footer)


@app.route('/read', methods=["POST"])
def read():
    contenido = ""
    datosGuardados = []
    navbar = '''
        <nav class="navbar navbar-expand-md nav-background">
            <div class="container"> 
                <a class="navbar-brand mx-auto k-font" href="/"><i class="fas fa-pizza-slice fa-fw"></i>HOME</a> 
            </div>
        </nav>
    '''
    if request.method == "POST":

        f = open("../tedecoco/app/files/names.txt", "r")
        a = f.read()
        f.close()
        names = json.loads(a)
        #print(names)
        title = names[0]
        #print(title)
        del names[0]
        print(names)
        

        txt = open('../tedecoco/app/files/names.txt'+str(title['name'])+'.txt', 'a+')
        
        for n in names:
            print(n)
            print(request.form[n['id']])
            print(n['name'] )
            datosGuardados.append(n['name'] + " : " + request.form[n['id']] + "\n")
            txt.write(n['name'] + " : " + request.form[n['id']] + "\n")
        txt.write('\n')
        txt.close()
        lista = []
        lista.append('''<h1 class="text-center w-100 mb-3">La información se ha guardado correctamente en un archivo de texto</h1>''')
        for i in datosGuardados:
            lista.append("<p>" + i + "</p>")

        for item in lista:
                        contenido += item + '\n'

        title = "Exito"
        return render_template("home.html", title=title, nav=navbar, page=contenido, foot=footer)

@app.route('/')
def home():
    title = "Home"

    navbar = '''
        <nav class="navbar navbar-expand-md nav-background">
            <div class="container"> 
                <a class="navbar-brand mx-auto k-font" href="/"><i class="fas fa-pizza-slice fa-fw"></i> Napoles</a> 
            </div>
        </nav>
    '''

    inputTitle = DivTitle("Seleccione un diagrama: ", "mx-auto h1 k-font")
    inputXML = Input("xml-file", "custom-file col-12 mb-3", "file",
                     "custom-file-input", "custom-file-label", "Upload file", "diagram")
    submitBtn = Button(1, "Enviar", "btn btn-custom k-font")
    tooltip = TP("1", "text-center d-flex align-items-center",
                 "fas fa-info-circle fa-fw fa-2x", "bottom", "Only .bpmn extensions", "")
    formXML = Form("w-100 row m-0 justify-content-center", "/upload", "POST",
                   "multipart/form-data", [inputXML, tooltip], submitBtn, ".bpmn")

    items = [inputTitle, formXML]

    contenido = ""
    for item in items:
        contenido += item.getHtml() + '\n'

    return render_template("home.html", title=title, nav=navbar, page=contenido, foot=footer)


if __name__ == "__main__":
    app.run(debug=True)
