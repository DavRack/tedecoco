from xml.dom import minidom
from xml.dom.minidom import parse

xmldoc = minidom.parse('Diagramas/AdoptameMIAU.bpmn')
Ventana = xmldoc.documentElement.childNodes
print(Ventana.item(1)._get_attributes())
for child in Ventana:
    child
#print(xmldoc.documentElement.childNodes) obtener los hijos
#print(xmldoc.documentElement.toprettyxml()) mostrar xml bonito
#print(xmldoc.documentElement.toxml()) mostrar todo el xml
# find the name element, if found return a list, get the first element
#name_element = xmldoc.getElementsByTagName("name")[0]

# this will be a text node that contains the actual text
#text_node = name_element.childNodes[0]

# get text
#print text_node.data