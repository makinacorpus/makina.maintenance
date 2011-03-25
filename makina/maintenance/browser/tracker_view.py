from Products.Five import BrowserView
class TrackerView(BrowserView):
    """..."""

    def credits(self):
        return str(self.context.getField('credits').get(self.context))
