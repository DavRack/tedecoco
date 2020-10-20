class DivTitle:
    def __init__(self, title, divClass):
        self.title = title
        self.divClass = divClass

    def getHtml(self):
        return '<div class="{0}">{1}</div>'.format(self.divClass, self.title)
