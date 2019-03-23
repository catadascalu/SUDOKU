from model.State import *
class BFS:

    def __init__(self, initial_state):
        self.__queue = []
        self.__initialState = initial_state

    def solve(self):
        visited = []

        self.__queue.append(self.__initialState)
        visited.append(self.__initialState)

        while(len(self.__queue) > 0):

            state = self.__queue.pop(0)

            if(state.isFinal()):
                return state

            found = False

            for i in range(0, state.getSize(), 1):
                if(found):
                    break
                for j in range(0, state.getSize(), 1):
                    if(found):
                        break
                    if(state.getValue(i, j) == 0):
                        found = True
                        for val in range(1, state.getSize() + 1, 1):
                            newState = State(state.getSize())
                            newState.copyState(state)
                            newState.complete(i, j, val)

                            if((newState.isValid(i, j)) and (newState not in visited)):
                                newState.setCompleted(newState.getCompleted() + 1)
                                self.__queue.append(newState)
                                visited.append(newState)
                                print(newState.toString())
                                break
                            '''elif(val == state.getSize()):
                                self.__stack.append(state)
                                break'''



        'return None'