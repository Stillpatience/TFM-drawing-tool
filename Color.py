class Color:
    def __init__(self, color, hexa=False):
        if hexa:
            self.color = color
        else:
            self.color = '%02x%02x%02x' % color[:3]
            try:
                self.alpha = color[3]
            except IndexError:
                self.alpha = None

    def __str__(self):
        if self.alpha == 0:
            return ""
        return self.color.lower()
