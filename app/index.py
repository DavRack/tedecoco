from flask import Flask, render_template, request
#import controllers.Firebase as fairbeis
import controllers.Parseo as Parce
from models.Button import Button
from models.DivTitle import DivTitle
from models.Dropdown import Dropdown
from models.Form import Form
from models.Input import Input
from models.Tooltip import Tooltip as TP
import re

navbar=""
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
    def __init__(self,icon,title):
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
                #path_on_cloud = "file.bpmn"
                #fairbeis.getStorage().child(path_on_cloud).put(xmlFile)
                #title = str(xmlFile.filename)
                #contenido = '''
                #    <h1 class="k-font w-100 text-center">{0}</h1>
                #'''.format(str(xmlFile.filename))

                title = xmlFile.filename

                if re.findall(r"\.{1}bpmn$", title):
                    # En esta área se interpreta el XML
                    #texto = Parce.returnTextAnnotation(xmlFile)
                    #text = Parce.returnTextAnnotation(xmlFile)
                    #asociation = Parce.returnAssociation(xmlFile)
                    dic=Parce.returnActivityElements(xmlFile)
                    #lanes = Parce.returnLanes(xmlFile) 
                    items = []
                    contenido = ""
                    for d in dic:
                        print(dic[d][0])
                        if ("Boton" in dic[d][0]):
                            items.append(Button(1,dic[d][1],"btn btn-custom k-font"))
                        elif ("Textbox" in dic[d][0]):
                            items.append(Input("id","col-12 mb-3","input","input",dic[d][1], dic[d][1],dic[d][1]))
                        elif ("Radio" in dic[d][0]):
                            items.append(Input("id","col-12 mb-3","radio","radio",dic[d][1], dic[d][1],dic[d][1]))
                        elif ("Desplegable" in dic[d][0]):
                            l = list(dic[d][1].split(","))
                            items.append(Dropdown(1,l[0],l))
                        elif ("Titulo" in dic[d][0]):
                            items.append(DivTitle(dic[d][1],"mx-auto h1 k-font"))
                        elif ("Navbar" in dic[d][0]):
                            navbar= (Navbar("fas fa-paw",dic[d][1])).getHtml()
                        else:
                            print(3)

                    for item in items:
                        contenido += item.getHtml() + '\n'

                    #contenido = ""
                    
                    #for te in dic:
                    #    contenido += "<h1 class='k-font w-100 text-center'>"+str(dic[te])+"</h1>\n"
                    #for lane in lanes:
                    #    contenido += "<h1 class='k-font w-100 text-center'>"+Parce.returnTextNode(lane)+"</h1>\n"
                    
                    return render_template("home.html", title=title, nav=navbar, page=contenido, foot=footer)
                else:
                    title = "Error"

                    contenido = '''
                        <h1 class="text-center w-100 mb-3">El archivo no es un diagrama BPMN</h1>
                        <a class="btn btn-custom mx-auto" href="/">Ir atrás</a>
                    '''

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

    navbar = '''
        <nav class="navbar navbar-expand-md nav-background">
            <div class="container"> 
                <a class="navbar-brand mx-auto k-font" href="/"><i class="fas fa-pizza-slice fa-fw"></i> Napoles</a> 
            </div>
        </nav>
    '''


    inputTitle = DivTitle("Seleccione un diagrama: ", "mx-auto h1 k-font")
    inputXML = Input("xml-file","custom-file col-12 mb-3","file","custom-file-input","custom-file-label", "Upload file", "diagram")
    submitBtn = Button(1, "Enviar", "btn btn-custom k-font")
    tooltip = TP("1","text-center d-flex align-items-center","fas fa-info-circle fa-fw fa-2x", "bottom", "Only .bpmn extensions","")
    formXML = Form("w-100 row m-0 justify-content-center","/upload", "POST", "multipart/form-data", [inputXML, tooltip], submitBtn, ".bpmn")
    

    items = [inputTitle, formXML]

    contenido = ""
    for item in items:
        contenido += item.getHtml() + '\n'

    return render_template("home.html", title=title, nav=navbar, page=contenido, foot=footer)


if __name__ == "__main__":
    app.run(debug=True)
