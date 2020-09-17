from xml.dom import minidom
from xml.dom.minidom import parse
import re
from collections import OrderedDict


def returnTextNode(Node):
    """
    Esta funcion lo que hace es retornar el texto contenido
    en un nodo mandado como parametro
    ej: <bpmn:text>Ingrese el nombre del gato</bpmn:text>
    return: Ingrese el nombre del gato
    """
    if type(Node) == "<class 'str'>":
        match = re.search(r"(\>(.*)\<)", str(Node))
    else:
        match = re.search(r"(\>(.*)\<)", str(Node.toxml()))
    return match.group()[1:-1]


def returnSequenceFlow(xmlFile):#nombreDelDiagrama):
    """
    Esta funcion lo que hace es retornar una lista
    que tiene los task(el simbolo actividad que es un rectangulo con bordes redondeados)
    ej: AdoptameMIAU4.0(nombre del diagrama)
    return: [<DOM Element: bpmn:task at 0x1e24268>,
    <DOM Element: bpmn:task at 0x1e24340>,
    <DOM Element: bpmn:task at 0x1e244f0>,
    <DOM Element: bpmn:task at 0x1e24a00>,
    <DOM Element: bpmn:task at 0x1e24e38>,
    <DOM Element: bpmn:task at 0x1e2e028>,
    <DOM Element: bpmn:task at 0x1e2e148>]
    """
    #ruta = "Diagramas/" + nombreDelDiagrama + ".bpmn"
    #xmldoc = minidom.parse(ruta)
    xmldoc = minidom.parse(xmlFile)
    Ventana = [
        x for x in list(xmldoc.documentElement.childNodes) if str(x.childNodes) != "()"
    ]
    Ventanas = [
        x for x in Ventana if "Process" in str(x._get_attributes().items()[0][1])
    ]
    App = [x for x in list(Ventanas[0].childNodes) if str(x.childNodes) != "()"]
    Elements = [x for x in App if "Flow" in str(x._get_attributes().items()[0][1])]
    return Elements


def returnLanes(xmlFile):#nombreDelDiagrama):
    """
    Esta funcion lo que hace es retornar una lista
    que tiene los lanes(las divisiones de los actores)
    ej: AdoptameMIAU4.0(nombre del diagrama)
    return: [<DOM Element: bpmn:lane at 0x3bcbbb0>,
    <DOM Element: bpmn:lane at 0x3bcbd18>,
    <DOM Element: bpmn:lane at 0x3bcbe80>,
    <DOM Element: bpmn:lane at 0x3bcbfa0>,
    <DOM Element: bpmn:lane at 0x3bd7070>]
    """
    #ruta = "Diagramas/" + nombreDelDiagrama + ".bpmn"
    #xmldoc = minidom.parse(ruta)
    xmldoc = minidom.parse(xmlFile)
    Ventana = [
        x for x in list(xmldoc.documentElement.childNodes) if str(x.childNodes) != "()"
    ]
    Ventanas = [
        x for x in Ventana if "Process" in str(x._get_attributes().items()[0][1])
    ]
    App = [x for x in list(Ventanas[0].childNodes) if str(x.childNodes) != "()"]
    Elements = [x for x in App if "LaneSet" in str(x._get_attributes().items()[0][1])]
    lanes = [x for x in list(Elements[0].childNodes) if str(x.childNodes) != "()"]
    return lanes


def getElementByNameDiagram(Nombre):
    prueba = [x for x in returnLanes(Nombre) if str(x.childNodes) != "()"]
    elementos = [x.childNodes for x in prueba]
    # este codigo me aplana una lista(convierte una lista de listas en lista)
    elementos = [item for lista in elementos for item in lista]
    elementos = [x.childNodes for x in elementos if str(x.childNodes) != "()"]
    elementos = [item for lista in elementos for item in lista]
    elementos = [x.wholeText for x in elementos]
    return elementos


# print(getElementByNameDiagram('AdoptameMIAU4.0'))


def returnActivity(xmlFile):#nombreDelDiagrama):
    """
    Esta funcion lo que hace es retornar una lista
    que tiene los task(el simbolo actividad que es un rectangulo con bordes redondeados)
    ej: AdoptameMIAU4.0(nombre del diagrama)
    return: [<DOM Element: bpmn:task at 0x1e24268>,
    <DOM Element: bpmn:task at 0x1e24340>,
    <DOM Element: bpmn:task at 0x1e244f0>,
    <DOM Element: bpmn:task at 0x1e24a00>,
    <DOM Element: bpmn:task at 0x1e24e38>,
    <DOM Element: bpmn:task at 0x1e2e028>,
    <DOM Element: bpmn:task at 0x1e2e148>]
    """
    #ruta = "Diagramas/" + nombreDelDiagrama + ".bpmn"
    #xmldoc = minidom.parse(ruta)
    xmldoc = minidom.parse(xmlFile)
    Ventana = [
        x for x in list(xmldoc.documentElement.childNodes) if str(x.childNodes) != "()"
    ]
    Ventanas = [
        x for x in Ventana if "Process" in str(x._get_attributes().items()[0][1])
    ]
    App = [x for x in list(Ventanas[0].childNodes) if str(x.childNodes) != "()"]
    Elements = [x for x in App if "Activity" in str(x._get_attributes().items()[0][1])]
    return Elements


# Este metodo es para extraer por tublas el id ddel activity, el nombre, y los flows y datastore que tienen relacionados


def returnTextAnnotation(xmlFile):#nombreDelDiagrama):
    """
    Esta funcion lo que hace es retornar una lista
    que tiene los task(el simbolo actividad que es un rectangulo con bordes redondeados)
    ej: AdoptameMIAU4.0(nombre del diagrama)
    return: [<DOM Element: bpmn:task at 0x1e24268>,
    <DOM Element: bpmn:task at 0x1e24340>,
    <DOM Element: bpmn:task at 0x1e244f0>,
    <DOM Element: bpmn:task at 0x1e24a00>,
    <DOM Element: bpmn:task at 0x1e24e38>,
    <DOM Element: bpmn:task at 0x1e2e028>,
    <DOM Element: bpmn:task at 0x1e2e148>]
    """
    #ruta = "Diagramas/" + nombreDelDiagrama + ".bpmn"
    #xmldoc = minidom.parse(ruta)
    xmldoc = minidom.parse(xmlFile)
    Ventana = [
        x for x in list(xmldoc.documentElement.childNodes) if str(x.childNodes) != "()"
    ]
    Ventanas = [
        x for x in Ventana if "Process" in str(x._get_attributes().items()[0][1])
    ]
    App = [x for x in list(Ventanas[0].childNodes) if str(x.childNodes) != "()"]
    Elements = [
        x for x in App if "TextAnnotation" in str(x._get_attributes().items()[0][1])
    ]
    dictionary = {
        i.getAttribute("id"): i.childNodes[1].firstChild.nodeValue for i in Elements
    }
    return dictionary


def returnAssociation(xmlFile):#nombreDelDiagrama):
    """
    Esta funcion lo que hace es retornar una lista
    que tiene los task(el simbolo actividad que es un rectangulo con bordes redondeados)
    ej: AdoptameMIAU4.0(nombre del diagrama)
    return: [<DOM Element: bpmn:task at 0x1e24268>,
    <DOM Element: bpmn:task at 0x1e24340>,
    <DOM Element: bpmn:task at 0x1e244f0>,
    <DOM Element: bpmn:task at 0x1e24a00>,
    <DOM Element: bpmn:task at 0x1e24e38>,
    <DOM Element: bpmn:task at 0x1e2e028>,
    <DOM Element: bpmn:task at 0x1e2e148>]
    """
    #ruta = "Diagramas/" + nombreDelDiagrama + ".bpmn"
    #xmldoc = minidom.parse(ruta)
    xmldoc = minidom.parse(xmlFile)
    Ventana = [
        x for x in list(xmldoc.documentElement.childNodes) if str(x.childNodes) != "()"
    ]
    Ventanas = [
        x for x in Ventana if "Process" in str(x._get_attributes().items()[0][1])
    ]
    App = [x for x in list(Ventanas[0].childNodes) if str(x.childNodes) != "()"]
    Elements = [
        x for x in App if "Association" in str(x._get_attributes().items()[0][1])
    ]
    dictionary1 = {
        i.getAttribute("sourceRef"): i.getAttribute("targetRef") for i in Elements
    }
    return dictionary1


# print(returnTextAnnotation('AdoptameMIAU4.0'))


# print(returnAssociation('AdoptameMIAU4.0'))


def returnActivityElements(xmlFile):#nombreDelDiagrama):
    # obtener el valor de cada
    Dic = {}
    # _get_localName me devuelve el nombre del nodo despues del bpmn:
    for i in returnActivity(xmlFile):#nombreDelDiagrama):
        flow = [z for z in i.childNodes if str(z.childNodes) != "()"]
        flow = [z.childNodes for z in flow]
        flow = [item for lista in flow for item in lista]
        flow = [
            z.wholeText
            for z in flow
            if "Text" in str(type(z)) and "\n" not in z.wholeText
        ]
        # print(flow)
        other = [z for z in i.childNodes if str(z.childNodes) != "()"]
        other = [z.childNodes for z in other]
        other = [item for lista in other for item in lista]
        other = [z for z in other if "Element" in str(type(z))]
        if other != []:
            other = [z.childNodes for z in other]
            other = [item for lista in other for item in lista]
            other = [x.wholeText for x in other]
        texto = returnTextAnnotation(xmlFile)#nombreDelDiagrama)
        asociation = returnAssociation(xmlFile)#nombreDelDiagrama)

        Dic[i.getAttribute("id")] = [
            i.getAttribute("name"),
            texto.get((asociation.get(i.getAttribute("id")))),
            flow,
            other,
        ]
        # aca devuelvo un diccionaro para acceder mas eficiente a los datos(por activityID).
    return Dic


# print(returnActivityElements('AdoptameMIAU4.0'))

# codigo que me devuelve los elementos de cada lane
def returnLanesWithElementsSorted(xmlFile):#nombreDelDiagrama):
    lista = [x.childNodes for x in returnLanes(xmlFile)]#nombreDelDiagrama)]
    listao = []
    Dic = {}
    for i in lista:
        a = [x for x in i if str(x.childNodes) != "()"]
        listao.append([x.firstChild.nodeValue for x in a])
    for i in range(0, len(listao)):
        listao[i].insert(0, returnLanes(xmlFile)[i].getAttribute("id"))#nombreDelDiagrama)[i].getAttribute("id"))
    Dic = {j: i[0] for i in listao for j in i}
    # diccionaro que me dice a que lane pertenece cada elemento por su ID
    secuencia = [
        [x.getAttribute("sourceRef"), x.getAttribute("targetRef")]
        for x in returnSequenceFlow(xmlFile)#nombreDelDiagrama)
    ]
    secuencias = [item for lista in secuencia for item in lista if "Activity" in item]
    Fernan = []
    acumulador = ""
    for i in secuencia:
        if Fernan == []:
            Fernan.append(i[1])
            acumulador = i[1]
        elif i[0] == acumulador and "Activity" in i[0] and "Activity" in i[1]:
            Fernan.append(i[1])
            acumulador = i[1]
    Elementoos = []
    acumulador = ""
    acuml = []
    contador = 1
    for i in Fernan:
        if acumulador == "":

            acuml.append(i)
            acumulador = Dic.get(i)
        elif Dic.get(i) == acumulador:
            acuml.append(i)
        else:
            acuml.insert(0, contador)
            Elementoos.append(acuml)
            acuml = []
            acumulador = Dic.get(i)
            contador += 1
            acuml.append(i)

    acuml.insert(0, contador)
    Elementoos.append(acuml)
    acuml = []
    # me devuelve una lista con los elementos de los lanes en orden grafico(como en el diagrama)
    # print(Elementoos)
    ElementosOrdenados = {"Linea " + str(i[0]): i[1:] for i in Elementoos}
    # diccionario donde la clave es la linea en orden y el valor el nombre de los activity
    return ElementosOrdenados


# ahora por ejemplo si queremos saber que elementos tiene al activity de la linea 1:
#for i in returnLanesWithElementsSorted('AdoptameMIAU4.0').get('Linea 5'):
#    print(returnActivityElements('AdoptameMIAU4.0').get(i))

# print(Fernan)
# elminina elementos repetidos de una lista
# secuencias = list(OrderedDict.fromkeys(secuencias))
# secuencias = [returnActivityElements("AdoptameMIAU4.0").get(i)[0] for i in Fernan]
# secuencias.insert(0, secuencia[0][0])
# print(secuencias)


# print(returnActivityElements("AdoptameMIAU4.0"))


def returnTextAnnotation(xmlFile):#nombreDelDiagrama):
    """
    Esta funcion lo que hace es retornar una lista
    que tiene los task(el simbolo actividad que es un rectangulo con bordes redondeados)
    ej: AdoptameMIAU4.0(nombre del diagrama)
    return: [<DOM Element: bpmn:task at 0x1e24268>,
    <DOM Element: bpmn:task at 0x1e24340>,
    <DOM Element: bpmn:task at 0x1e244f0>,
    <DOM Element: bpmn:task at 0x1e24a00>,
    <DOM Element: bpmn:task at 0x1e24e38>,
    <DOM Element: bpmn:task at 0x1e2e028>,
    <DOM Element: bpmn:task at 0x1e2e148>]
    """
    #ruta = "Diagramas/" + nombreDelDiagrama + ".bpmn"
    #xmldoc = minidom.parse(ruta)
    xmldoc = minidom.parse(xmlFile)
    Ventana = [
        x for x in list(xmldoc.documentElement.childNodes) if str(x.childNodes) != "()"
    ]
    Ventanas = [
        x for x in Ventana if "Process" in str(x._get_attributes().items()[0][1])
    ]
    App = [x for x in list(Ventanas[0].childNodes) if str(x.childNodes) != "()"]
    Elements = [
        x for x in App if "TextAnnotation" in str(x._get_attributes().items()[0][1])
    ]
    return Elements


# secuencias = [texto.get(i) for i in secuencias]
# secuencias.insert(0,secuencia[0][0])
# print(returnTextAnnotation('AdoptameMIAU4.0'))
# print(returnTextAnnotation('AdoptameMIAU4.0')[0].getAttribute('id')) #obtener el id
# print(returnTextAnnotation('AdoptameMIAU4.0')[0].childNodes[1].firstChild.nodeValue)
# obtener el valor de cada


# Lista.append((i.getAttribute('id'),i.getAttribute('name'),hola))
# print(Lista)

# print(returnActivity('AdoptameMIAU4.0')[0].getAttribute('name'))
# mostrar el atributo id y name del bpmn:task
# print(returnActivity('AdoptameMIAU4.0')[0]._get_attributes().items())

# Intento de dicomprehension
# a = {str(i):j for i in [1,2,3,4,5] for j in [2,4,6,8,10]}
# print(a)


# leer el  xml como un DOM Element(facilita muchisimos las cosas a la hora de parsear)
# xmldoc = minidom.parse('Diagramas/AdoptameMIAU.bpmn')
# print(type(xmldoc.documentElement.childNodes[0]))
# este codigo es para mostrar la cantidad de nodos hijos totales de todo el xml(en general)
# Ventana = [x for x in  list(xmldoc.documentElement.childNodes) if str(x.childNodes) != '()']
# Este codigo es para encontrar todas las ventanas sin importar la cantidad
# Ventanas = [x for x in Ventana if 'Process' in str(x._get_attributes().items()[0][1])]
# Ventana1 = Ventanas[0]
# print("1")
# App = [x for x in  list(Ventana1.childNodes) if str(x.childNodes) != '()']
# print('LaneSet' in str(App[0]._get_attributes().items()[0][1]))
# E = App.filter(lambda x: )
# Elements = [x for x in  App if 'LaneSet' in str(x._get_attributes().items()[0][1])]

# print(Elements[0].childNodes) #aqui estan los nombres y id de los elementosl
# lanes = [x for x in  list(Elements[0].childNodes) if str(x.childNodes) != '()']
# hijoslanes1 = lanes[0].getElementsByTagName("bpmn:flowNodeRef")


# la idea es hacer el arbol asi
# Arbol = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

# print( 'Process' in str(Ventana[1]._get_attributes().items()[0][1]))
# listadepurada = [x.childNodes for x in  Ventana if str(x.childNodes) != '()']
# print(listadepurada)


# print(str(Ventana.item(1).childNodes.item(1).childNodes) != '()' condicion de que si tiene hijo
# print(Ventana.item(1)._get_attributes().items())
# print(xmldoc.documentElement.childNodes) obtener los hijos
# print(xmldoc.documentElement.toprettyxml()) mostrar xml bonito
# print(xmldoc.documentElement.toxml()) mostrar todo el xml
# find the name element, if found return a list, get the first element
# name_element = xmldoc.getElementsByTagName("name")[0]

# this will be a text node that contains the actual text
# text_node = name_element.childNodes[0]

# get text
# print text_node.data
