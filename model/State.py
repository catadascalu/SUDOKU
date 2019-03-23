import math
import copy

class State:

    '''
    defines the state of the game at a certain point
    the board will be represented as a matrix
    retains the size of the matrix, the number of already completed cells, and the matrix
    if matrix[i][j] = 0 ==> empty cell

    initial state : read from file
    final state : completed matrix with no conflict on lines/columns/blocks
    '''
    def __init__(self, n):
        self.__n = n
        self.__completed = 0
        'self.__values = [[], [], [], [], [], [], [], [], []]'
        self.__values = []


    def copyState(self, s):
        's is another State'

        self.__n = s.__n
        self.__completed = s.__completed;
        for i in range(0, self.__n, 1):
            'for j in range(0, self.__n, 1):'
            self.__values.append([])
            self.__values[i] = copy.deepcopy(s.__values[i])

    def getCompleted(self):
        return self.__completed

    def setCompleted(self, c):
        self.__completed = c

    def isFinal(self):
        if(self.__completed == self.__n * self.__n):
            return True
        return False

    'values[line][column] is the cell where the last modification was made'
    def isValid(self, line, column):

        'if we find the same value on the line'
        for i in range(0, self.__n, 1):
            if((i != line) and (self.__values[i][column] == self.__values[line][column])):
                return False
        'if we find the same value on the column'
        for j in range(0, self.__n, 1):
            if((j != column) and (self.__values[line][j] == self.__values[line][column])):
                return False

        'check for conflicts in the block'

        r = int(math.sqrt(self.__n))
        line_start = line//r
        column_start = column//r

        if(line % r == 0): line_start = line_start
        if(column % r == 0): column_start = column_start

        line_start = line_start * r
        column_start = column_start * r

        line_end = line_start + r - 1
        column_end = column_start + r - 1

        for i in range(line_start, line_end + 1, 1):
            for j in range(column_start, column_end + 1, 1):
                if((i != line) and (j != column) and (self.__values[i][j] == self.__values[line][column])):
                    return False

        return True

    def complete(self, line, column, value):
        if((line >= 0) and (line <= self.__n) and (column >= 0) and (column <= self.__n)):
           ''' if(self.__values[line][column] == 0):
                self.__completed = self.__completed + 1'''
        self.__values[line][column] = value;


    def getSize(self):
        return self.__n;

    def getValue(self, line, column):
        return self.__values[line][column]

    def equals(self, s):
        if(self.__n != s.__n):
            return False
        for i in range(0, self.__n, 1):
            for j in range(0, self.__n, 1):
                if(self.__values[i][j] != s.__values[i][j]):
                    return False
        return True

    def toString(self):
        s = "";
        for i in range(0, self.__n, 1):
            for j in range(0, self.__n, 1):
                s = s + str(self.__values[i][j]) + " "

            s = s + '\n'

        return s

    def readStateFromFile(self, filename):
        file = open(filename, "r")

        i = 0
        for line in file:
            numbers = line.split(" ")
            '''
            for j in range (0, len(numbers), 1):
                self.__values[i].append(numbers[j])
            i = i + 1
            '''
            self.__values.append([])
            for j in numbers:

                self.__values[i].append(int(j))
                if( int(j) > 0) : self.__completed = self.__completed + 1
            i = i + 1

        file.close()
