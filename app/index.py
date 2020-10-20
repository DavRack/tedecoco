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
                
                    lanes = Parce.returnLanes(xmlFile)

                    contenido = ""
                    
                    for lane in lanes:
                        contenido += "<h1 class='k-font w-100 text-center'>"+Parce.returnTextNode(lane)+"</h1>\n"
                    
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
