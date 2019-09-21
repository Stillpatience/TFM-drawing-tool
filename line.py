class Line:
    def __init__(self, point1, point2, color, thickness, ):
        self.point1 = point1
        self.point2 = point2
        self.color = color
        self.thickness = thickness

    def __str__(self):
        return "<JD " + "P1=" + '"' + str(self.point1) + '"' + "P2=" + '"' + str(
            self.point2
        ) + '"' + 'c="' + str(self.color) + "," + str(self.thickness) + '"/>' if str(self.color) != "" else ""
