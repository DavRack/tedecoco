from xml.dom import minidom
from xml.dom.minidom import parse
import re


def returnTextNode(Node):
    """
    Esta funcion lo que hace es retornar el texto contenido
    en un nodo mandado como parametro
    ej: <bpmn:text>Ingrese el nombre del gato</bpmn:text>
    return: Ingrese el nombre del gato
    """
    if type(Node) == "<class 'str'>":
        match = re.search(r'(\>(.*)\<)', str(Node))
    else:
        match = re.search(r'(\>(.*)\<)', str(Node.toxml()))
    return match.group()[1:-1]


def returnLanes(nombreDelDiagrama):
    """
    Esta funcion lo que hace es retornar una lista
    que tiene los lanes(las divisiones de los actores)
    ej: AdoptameMIAU2.0(nombre del diagrama)
    return: [<DOM Element: bpmn:lane at 0x3bcbbb0>,
    <DOM Element: bpmn:lane at 0x3bcbd18>,
    <DOM Element: bpmn:lane at 0x3bcbe80>,
    <DOM Element: bpmn:lane at 0x3bcbfa0>,
    <DOM Element: bpmn:lane at 0x3bd7070>]
    """
    ruta = 'Diagramas/' +nombreDelDiagrama+'.bpmn'
    xmldoc = minidom.parse(ruta)
    Ventana = [x for x in  list(xmldoc.documentElement.childNodes) if str(x.childNodes) != '()']
    Ventanas = [x for x in Ventana if 'Process' in str(x._get_attributes().items()[0][1])]
    App = [x for x in  list(Ventanas[0].childNodes) if str(x.childNodes) != '()']
    Elements = [x for x in  App if 'LaneSet' in str(x._get_attributes().items()[0][1])]
    lanes = [x for x in  list(Elements[0].childNodes) if str(x.childNodes) != '()']
    return lanes
    
def getElementByNameDiagram(Nombre):
    prueba = [ x for x in returnLanes(Nombre) if str(x.childNodes) != '()']
    elementos = [x.childNodes for x in prueba ]
    #este codigo me aplana una lista(convierte una lista de listas en lista)
    elementos = [item for lista in elementos for item in lista]
    elementos = [x.childNodes for x in elementos if str(x.childNodes) != '()']
    elementos = [item for lista in elementos for item in lista]
    elementos = [x.wholeText for x in elementos]
    return elementos

#print(getElementByNameDiagram('AdoptameMIAU2.0'))

def returnActivity(nombreDelDiagrama):
    """
    Esta funcion lo que hace es retornar una lista
    que tiene los task(el simbolo actividad que es un rectangulo con bordes redondeados)
    ej: AdoptameMIAU2.0(nombre del diagrama)
    return: [<DOM Element: bpmn:task at 0x1e24268>, 
    <DOM Element: bpmn:task at 0x1e24340>, 
    <DOM Element: bpmn:task at 0x1e244f0>, 
    <DOM Element: bpmn:task at 0x1e24a00>, 
    <DOM Element: bpmn:task at 0x1e24e38>, 
    <DOM Element: bpmn:task at 0x1e2e028>, 
    <DOM Element: bpmn:task at 0x1e2e148>]
    """
    ruta = 'Diagramas/' +nombreDelDiagrama+'.bpmn'
    xmldoc = minidom.parse(ruta)
    Ventana = [x for x in  list(xmldoc.documentElement.childNodes) if str(x.childNodes) != '()']
    Ventanas = [x for x in Ventana if 'Process' in str(x._get_attributes().items()[0][1])]
    App = [x for x in  list(Ventanas[0].childNodes) if str(x.childNodes) != '()']
    Elements = [x for x in  App if 'Activity' in str(x._get_attributes().items()[0][1])]
    return Elements


#Este metodo es para extraer por tublas el id ddel activity, el nombre, y los flows y datastore que tienen relacionados

Lista = []
#_get_localName me devuelve el nombre del nodo despues del bpmn:
for i in returnActivity('AdoptameMIAU2.0'):
    flow = [z for z in i.childNodes if str(z.childNodes) != '()' ]
    flow = [z.childNodes for z in flow]
    flow = [item for lista in flow for item in lista]
    flow = [z.wholeText for z in flow if 'Text' in str(type(z)) and '\n' not in z.wholeText]
    #print(flow)
    other = [z for z in i.childNodes if str(z.childNodes) != '()' ]
    other = [z.childNodes for z in other]
    other = [item for lista in other for item in lista]
    other = [z for z in other if 'Element' in str(type(z))]
    if other != [] :
        other = [z.childNodes for z in other]
        other = [item for lista in other for item in lista]
        other = [x.wholeText for x in other]
    Lista.append((i.getAttribute('id'),i.getAttribute('name'),flow,other))
print(Lista)

#Lista.append((i.getAttribute('id'),i.getAttribute('name'),hola))
#print(Lista)

#print(returnActivity('AdoptameMIAU2.0')[0].getAttribute('name'))
#mostrar el atributo id y name del bpmn:task
#print(returnActivity('AdoptameMIAU2.0')[0]._get_attributes().items())

#Intento de dicomprehension
#a = {str(i):j for i in [1,2,3,4,5] for j in [2,4,6,8,10]}
#print(a)


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
