#!/usr/bin/python3
from xml.dom import minidom
from xml.dom.minidom import parse
path = "diagram/test.bpmn"

# leer archivo en y guardarlo en "archivoXml"

archivoXml = open(path,"r")
root = et.fromstring(archivoXml.read())

print(type(root.items()[0][1]))
