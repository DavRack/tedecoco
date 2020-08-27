from xml.dom import minidom
from xml.dom.minidom import parse

#leer el  xml como un DOM Element(facilita muchisimos las cosas a la hora de parsear)
xmldoc = minidom.parse('Diagramas/AdoptameMIAU2.0.bpmn')
#este codigo es para mostrar la cantidad de nodos hijos totales de todo el xml(en general)
Ventana = [x for x in  list(xmldoc.documentElement.childNodes) if str(x.childNodes) != '()']
print(Ventana)
#Este codigo es para encontrar todas las ventanas sin importar la cantidad
Ventanas = [x for x in Ventana if 'Process' in str(x._get_attributes().items()[0][1])]
Ventana1 = Ventanas[0]
print("1")
App = [x for x in  list(Ventana1.childNodes) if str(x.childNodes) != '()']
print('LaneSet' in str(App[0]._get_attributes().items()[0][1]))
#E = App.filter(lambda x: )
Elements = [x for x in  App if 'LaneSet' in str(x._get_attributes().items()[0][1])]

print(Elements) #aqui estan los nombres y id de los elementos
#la idea es hacer el arbol asi
#Arbol = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

#print( 'Process' in str(Ventana[1]._get_attributes().items()[0][1]))
#listadepurada = [x.childNodes for x in  Ventana if str(x.childNodes) != '()']
#print(listadepurada)


# print(str(Ventana.item(1).childNodes.item(1).childNodes) != '()' condicion de que si tiene hijo
# print(Ventana.item(1)._get_attributes().items())
#print(xmldoc.documentElement.childNodes) obtener los hijos
#print(xmldoc.documentElement.toprettyxml()) mostrar xml bonito
#print(xmldoc.documentElement.toxml()) mostrar todo el xml
# find the name element, if found return a list, get the first element
#name_element = xmldoc.getElementsByTagName("name")[0]

# this will be a text node that contains the actual text
#text_node = name_element.childNodes[0]

# get text
#print text_node.data