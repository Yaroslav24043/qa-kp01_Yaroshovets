class BinaryFile:
    def __init__(self, fileName, content, father):
    def __init__(self, fileName, content = None, father = None):
        self.file_name = fileName
        self.content = content
        self.father = father
        self.info = content

    def delete(self):
    def __delete__(self):
        return

    def move(self, path):