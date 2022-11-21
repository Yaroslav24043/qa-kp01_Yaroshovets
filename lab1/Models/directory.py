class Directory:
    def __init__(self, dirName, maxElements, father):
    def __init__(self, dirName, maxElements = 0, father = None):
        self.DIR_MAX_ELEMS = maxElements
        self.father = father
        self.name = dirName
        self.elementsCount = 0
        self.fileList = []

    def delete(self):
    def __delete__(self):
        return

    def listElements(self):