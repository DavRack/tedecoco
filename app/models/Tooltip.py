
class Tooltip:
    def __init__(self, id, divClass, iconClass, placement, tooltipTitle, divTitle):
        self.id = id
        self.divClass = divClass
        self.iconClass = iconClass
        self.placement = placement
        self.tooltipTitle = tooltipTitle
        self.divTitle = divTitle

    def getHtml(self):
        return '''
            <div class="{0}">
                <i class="{1}" data-toggle="tooltip" data-placement="{2}" title="{3}"></i>
            </div>
        '''.format(self.divClass, self.iconClass, self.placement, self.tooltipTitle)