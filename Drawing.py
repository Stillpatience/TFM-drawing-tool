class Drawing:
    def __init__(self, lines):
        self.lines = lines

    def __str__(self):
        result = "<C><P/><Z><S /><D /><O /><L>"
        for line in self.lines:
            result += str(line)
        result += "<L /></L></Z></C>"
        return result
