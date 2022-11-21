class BufferFile:
    def __init__(self, maxSize, fileName, father):
    def __init__(self, fileName,maxSize = 0, father = None):
        self.MAX_BUF_FILE_SIZE = maxSize
        self.fileName = fileName
        self.father = father
        self.info = []
        self.content = []

    def delete(self):
    def __delete__(self):
        return

    def move(self, path):