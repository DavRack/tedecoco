#!/usr/bin/python3
import xml.etree.cElementTree as et
path = "diagram/test.bpmn"

# leer archivo en y guardarlo en "archivoXml"

archivoXml = open(path,"r")
root = et.fromstring(archivoXml.read())

print(type(root.items()[0][1]))
