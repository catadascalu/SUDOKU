from model.State import *

class GBFS:

    def __init__(self, initial_state):
        self.__queue = []
        self.__initialState = initial_state
        self.__minValueList = [[[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []]]
        self.__valueList = [[], [], [], [], [], [], [], [], []]

    def initialiseValueLists(self):
        testState = State(self.__initialState.getSize())
        testState.copyState(self.__initialState)
        for i in range(0, self.__initialState.getSize(), 1):
            for j in range(0, self.__initialState.getSize(), 1):
                if(self.__initialState.getValue(i, j) != 0):
                    self.__valueList[i].append(0);
                else:
                    values = 0
                    for val in range(1, self.__initialState.getSize() + 1, 1):
                        newState = State(testState.getSize())
                        newState.copyState(testState)
                        newState.complete(i, j, val)
                        if(newState.isValid(i, j)):
                            values = values + 1
                    self.__valueList[i].append(values)

    def updateValueList(self, state):
        testState = State(state.getSize())
        testState.copyState(state)
        for i in range(0, state.getSize(), 1):
            for j in range(0, state.getSize(), 1):
                if(state.getValue(i, j) == 0):
                    values = 0
                    for val in range(1, state.getSize() + 1, 1):
                        newState = State(testState.getSize())
                        newState.copyState(testState)
                        newState.complete(i, j, val)
                        if(newState.isValid(i, j)):
                            values = values + 1
                    self.__valueList[i][j] = values



    def solve(self):
        visited = []

        self.__queue.append(self.__initialState)
        visited.append(self.__initialState)

        while(len(self.__queue) > 0):

            state = self.__queue.pop(0)

            if(state.isFinal()):
                return state

            min = 10
            k = 9
            l = 9
            for i in range(0, state.getSize(), 1):
                for j in range(0, state.getSize(), 1):
                    if(self.__valueList[i][j] < min and self.__valueList[i][j] > 0):
                        min = self.__valueList[i][j]
                        k = i
                        l = j
            if(k < 9 and l < 9):
                if(state.getValue(k, l) == 0):
                    for val in range(1, state.getSize() + 1, 1):
                        newState = State(state.getSize())
                        newState.copyState(state)
                        newState.complete(k, l, val)

                        if ((newState.isValid(k, l)) and (newState not in visited)):
                            newState.setCompleted(newState.getCompleted() + 1)
                            self.__valueList[k][l] = 0
                            self.__queue.append(newState)
                            visited.append(newState)
                            self.updateValueList(newState)
                            print(newState.toString())
                            break
