class Form:
    def __init__(self,formClass,action,method,encType,inputs,submit,extension):
        self.formClass = formClass
        self.action = action
        self.method = method
        self.encType = encType
        self.inputs = inputs
        self.submit = submit.getHtml()
        self.extension = extension

    def getHtml(self):
        lista = ""
        for div in self.inputs:
            lista += div.getHtml() + "\n"
        return '''
            <form class="{0}" action="{1}" method="{2}" enctype="{3}" accept="{6}">
                {4}                
                {5}
            </form>'''.format(self.formClass, self.action, self.method, self.encType, lista, self.submit, self.extension)
