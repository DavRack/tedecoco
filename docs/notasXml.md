# Notas sobre la estructura del archivo xml entregado por bpmn.io

## Definiciones

+ "laneSet" equivale a un "actor"
+ "lane" es un "sub Actor"
+ Definimos como "símbolo" todas las figuritas del diagrama ej: los cuadraditos, los rombitos, las hojitas etc... 

**Dentro de cada subactor (lane) se definen que símbolos que id´s contienen de
la siguiente manera:** 

+ (nombre del simbolo)_(id del simbolo)

Por ejemplo:

+ Event_0dmn4pd

donde "Event" es el nombre del símbolo y "0dmn4pd" es su id


**Ejemplo de un lane**

```{}
<bpmn:lane id="Lane_0f4jr24">
  <bpmn:flowNodeRef>Activity_06djsti</bpmn:flowNodeRef>
  <bpmn:flowNodeRef>Gateway_1e7mbw6</bpmn:flowNodeRef>
  <bpmn:flowNodeRef>Event_0dmn4pd</bpmn:flowNodeRef>
  <bpmn:flowNodeRef>Activity_0k1lxos</bpmn:flowNodeRef>
</bpmn:lane>
```
