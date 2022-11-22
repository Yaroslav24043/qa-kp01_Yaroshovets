import pytest
from directory import Directory
from binaryFile import BinaryFile
from logTextFile import LogTextFile
from bufferFile import BufferFile
from types import NoneType



class TestDirectory:
    fatherDirectory = Directory('fatherDir', 10)

    def test_directoryCreation(self):
        #arrange
        maxElements = 10
        name = 'name1'
        directory = Directory(name, maxElements)

        #act
        #assert
        assert directory.name == name
        assert directory.DIR_MAX_ELEMS == maxElements
        assert directory.elementsCount == 0
        assert type(directory.father) is NoneType
        assert type(directory.listElements()) is str

    def test_directoryMove(self):
        #arrange
        directory = Directory('dir')
        assert type(directory.father) is NoneType

        #act
        directory.move(self.fatherDirectory)

        #assert
        assert directory.father == self.fatherDirectory

    def test_directoryDeletion(self):
        #arrange
        directory = Directory('dir')

        #act
        del directory

        #assert
        assert 'directory' not in locals()

class TestBinary:
    fatherDirectory = Directory('fatherDir',10)

    def test_binaryCreation(self):
        #arrange
        name = 'name1'
        content = 'some file content blah blah blah'
        binary = BinaryFile(name, content, self.fatherDirectory)

        #act
        #assert
        assert binary.fileName == name
        assert binary.content == content
        assert binary.read() == content
        assert binary.father == self.fatherDirectory

    def test_binaryMove(self):
        #arrange
        name = 'name1'
        content = 'some file content blah blah blah'
        binary = BinaryFile(name, content)
        assert type(binary.father) is NoneType

        #act
        binary.move(self.fatherDirectory)

        #assert
        assert binary.father == self.fatherDirectory

    def test_binaryDeletion(self):
        #arrange
        binary = BinaryFile('bin')

        #act
        del binary

        #assert
        assert 'binary' not in locals()

class TestBuffer:
    fatherDirectory = Directory('fatherDir',10)

    def test_bufferCreation(self):
        #arrange
        name = 'name1'
        size = 10
        buffer = BufferFile(name, size, self.fatherDirectory)

        #act
        #assert
        assert buffer.fileName == name
        assert buffer.MAX_BUF_FILE_SIZE == size
        assert pytest.raises(OverflowError)
        assert buffer.father == self.fatherDirectory

    def test_bufferMove(self):
        #arrange
        name = 'name1'
        content = 'some file content blah blah blah'
        buffer = BufferFile(name, content)
        assert type(buffer.father) is NoneType

        #act
        buffer.move(self.fatherDirectory)

        #assert
        assert buffer.father == self.fatherDirectory

    def test_bufferDeletion(self):
        #arrange
        buffer = BufferFile('buffer')

        #act
        del buffer

        #assert
        assert 'buffer' not in locals()

    def test_bufferAddConsume(self):
        #arrange
        name = 'name1'
        size = 10
        line1 = 'line1'
        line2 = 'line2'
        buffer = BufferFile(name, size)

        #act
        buffer.push(line1)
        buffer.push(line2)


        #assert
        assert buffer.consume() == line1
        assert buffer.consume() == line2
        assert pytest.raises(OverflowError)

class TestLog:
    fatherDirectory = Directory('fatherDir',10)

    def test_logCreation(self):
        #arrange
        name = 'name1'
        log = LogTextFile(name, self.fatherDirectory)

        #act
        #assert
        assert log.fileName == name
        assert log.read() ==''
        assert log.father == self.fatherDirectory

    def test_logMove(self):
        #arrange
        name = 'name1'
        log = LogTextFile(name)
        assert type(log.father) is NoneType

        #act
        log.move(self.fatherDirectory)

        #assert
        assert log.father == self.fatherDirectory

    def test_logDeletion(self):
        #arrange
        log = LogTextFile('log')

        #act
        del log

        #assert
        assert 'log' not in locals()

    def test_logAddRead(self):
        #arrange
        name = 'name1'
        line1 = 'line1'
        line2 = 'line2'
        log = LogTextFile(name)

        #act
        log.addLog(line1)
        log.addLog(line2)


        #assert
        assert log.read() == line1 + '\n' + line2 + '\n'