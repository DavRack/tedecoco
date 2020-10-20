class Button:
    def __init__(self, id, title, style):
        self.id = id
        self.title = title
        self.style = style

    def getHtml(self):
        return '<button class="{0}">{1}</button>'.format(self.style, self.title)