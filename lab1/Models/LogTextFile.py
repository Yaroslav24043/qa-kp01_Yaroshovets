class LogTextFile:
    def __init__(self, fileName, content, father):
    def __init__(self, fileName, father = None):
        self.fileName = fileName
        self.father = father
        self.info = content
        self.content = []

    def delete(self):
        return
    def move(self, path):
        return
    def read(self):
        return

    def appendLine(self, newLine):
    def addLog(self, newLine):
        return