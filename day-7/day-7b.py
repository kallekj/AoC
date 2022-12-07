import re


class File:

    def __init__(self, name, size, parentDir) -> None:
        self.parentDir = parentDir
        self.size = size
        self.name = name

    def toString(self):
        return f'name: {self.name}, size: {self.size}, parent: {self.parentDir.name}'

    def toDict(self):
        return {self.name: {'size': self.size, 'parentDir': self.parentDir.name}}


class Dir:

    def __init__(self, name, parentDir=None) -> None:
        self.name = name
        self.parentDir = parentDir
        self.size = 0
        self.files = {}
        self.dirs = {}

    def addFile(self, name, size):
        theFile = File(name, int(size), self)
        self.files[theFile.name] = theFile
        self.size += theFile.size
        self.updateParentSize(theFile)

    def getAllParents(self):
        if self.parentDir:
            return [self.parentDir] + self.parentDir.getAllParents()
        return [self.parentDir]

    def updateParentSize(self, file):
        for parent in self.getAllParents():
            if parent:
                parent.size += file.size

    def addDir(self, name):
        theDir = Dir(name, self)
        self.dirs[theDir.name] = theDir

    def getFileNames(self):
        return [file.name for file in self.files]

    def ls(self):
        return self.files + self.dirs

    def cd(self, name):
        return self.dirs[name]

    def toString(self):
        return f'name: {self.name}, size: {self.size}, files: {[item.toString() for item in self.files]} dirs: {[self.dirs[item].toString() for item in self.dirs]}'

    def toDict(self):
        files = {}
        dirs = {}
        for fileKey in self.files:
            fileDict = self.files[fileKey].toDict()
            files[fileKey] = fileDict
        for dirKey in self.dirs:
            dirDict = self.dirs[dirKey].toDict()
            dirs[dirKey] = dirDict
        return {self.name: {'size': self.size, 'files': files, 'dirs': dirs}}


fileSystem = Dir('/')
dirStack = []
currentDir = fileSystem
previousDir = currentDir


def cd(key):
    global currentDir
    global fileSystem
    global dirStack
    global previousDir
    if (key == '..'):
        currentDir = dirStack.pop()
    else:
        if (key == '/'):
            currentDir = fileSystem
        else:
            previousDir = currentDir
            currentDir = previousDir.cd(key)
            dirStack.append(previousDir)


def parseCommand(command):
    command = command.split(' ')
    if (command[0] == '$'):
        match command[1]:
            case 'cd':
                cd(command[2])
            case 'ls':
                pass
            case _:
                print(f'Unknown command {command[1]}')
    elif (re.match(r'\d', command[0])):
        currentDir.addFile(command[1], command[0])
    else:
        currentDir.addDir(command[1])


def getDirSizes(theDir: Dir):
    if len(theDir.dirs) > 0:
        return [theDir.size] + [getDirSizes(nextDir) for nextDir in theDir.dirs.values()]
    return [theDir.size]


def flatten(dirSizes):
    if isinstance(dirSizes, (list)):
        for nextDirSize in dirSizes:
            yield from flatten(nextDirSize)
    else:
        yield dirSizes


def getPossibleFilesToDeleteLessThanSize(theDir, usedSpace, size):
    def lessThanSize(a):
        freeSpace = 70000000 - usedSpace
        return (freeSpace + a) >= size
    return list(filter(lessThanSize, theDir))


with open('./day-7/input') as f:
    commands = [line.rsplit('\n') for line in f.readlines()]

for command in commands:
    parseCommand(command[0])


dirSizes = list(flatten(getDirSizes(fileSystem)))

usedSpace = fileSystem.size

dirsLessThanSize = sorted(
    getPossibleFilesToDeleteLessThanSize(dirSizes, usedSpace, 30000000))

print(dirsLessThanSize[0])
