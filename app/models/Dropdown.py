class Dropdown:
    def __init__(self, id, title, items):
        self.id = id
        self.title = title
        self.items = items

    def getHtml(self):
        lista = ""
        c = 0
        for i in self.items:
            lista += '<option value="{0}">{1}</option>'.format(c, i)
            c+=1

        return '''
            <select class="custom-select my-2 col-6 mx-auto">
                <option selected>{0}</option>
                {1}
            </select>'''.format(self.title, lista)
