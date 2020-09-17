from flask import Flask, render_template, request
import controllers.Firebase as fairbeis
import controllers.Parseo as Parce
from models.Button import Button
from models.DivTitle import DivTitle
from models.Dropdown import Dropdown
from models.Form import Form
from models.Input import Input

navbar = '''
    <nav class="navbar navbar-expand-md nav-background">
        <div class="container"> 
            <a class="navbar-brand mx-auto k-font" href="/"><i class="fas fa-pizza-slice fa-fw"></i> Napoles</a> 
        </div>
    </nav>
'''

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
app = Flask(__name__)

@app.route('/upload', methods=["POST"])
def upload():    
    if request.method == "POST":
        if request.files:
            if(request.files['diagram'].filename != ""):
                xmlFile = request.files['diagram']
                #path_on_cloud = "file.bpmn"
                #fairbeis.getStorage().child(path_on_cloud).put(xmlFile)
                #title = str(xmlFile.filename)
                #contenido = '''
                #    <h1 class="k-font w-100 text-center">{0}</h1>
                #'''.format(str(xmlFile.filename))

                lanes = Parce.returnLanes(xmlFile)

                contenido = ""
                for lane in lanes:
                    contenido += "<h1 class='k-font w-100 text-center'>"+Parce.returnTextNode(lane)+"</h1>\n"
                title = "Lanes"
                
                
                return render_template("home.html", title=title, nav=navbar, page=contenido, foot=footer)      
            else:
                title = "Error"
                contenido = '''
                    <h1 class="text-center w-100 mb-3">No se seleccionó diagrama</h1>
                    <a class="btn btn-custom mx-auto" href="/">Ir atrás</a>
                '''
                return render_template("home.html", title=title, nav=navbar, page=contenido, foot=footer)   
            

@app.route('/')
def home():
    title = "Home"

    inputTitle = DivTitle("Seleccione un diagrama: ", "mx-auto h1 k-font")
    inputXML = Input("xml-file","custom-file col-12 mb-3","file","custom-file-input","custom-file-label", "Upload file", "diagram")
    submitBtn = Button(1, "Enviar", "btn btn-custom k-font mx-auto")
    formXML = Form("w-100 row m-0","/upload", "POST", "multipart/form-data", [inputXML], submitBtn, ".bpmn")

    items = [inputTitle, formXML]

    contenido = ""
    for item in items:
        contenido += item.getHtml() + '\n'

    return render_template("home.html", title=title, nav=navbar, page=contenido, foot=footer)


if __name__ == "__main__":
    app.run(debug=True)
