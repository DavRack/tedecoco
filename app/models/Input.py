class Input:
    def __init__(self, id, divClass, inputType, inputClass, labelClass, title, name):
        self.id = id
        self.title = title
        self.divClass = divClass
        self.inputType = inputType
        self.inputClass = inputClass
        self.labelClass = labelClass
        self.name = name

    def getHtml(self):
        return '''<div class="{0}">
                <label class="{4}" for="{3}">{5}</label>
                <input type="{1}" class="{2}" id={3} name={6}>
            </div>
        '''.format(self.divClass, self.inputType, self.inputClass, self.id, self.labelClass, self.title, self.name)
        
