from controller.BFS import *
from controller.GBFS import *
from model.State import *

class main():
    def run(self):

        n = input("Enter game size(must be a perfect square number): ")


        if n == '9':
            initial_state = State(int(n))
            initial_state.readStateFromFile("sudokuElementary.txt")

            print("Initial state: \n")
            print(initial_state.toString())

            option = input("Enter game method (bfs / gbfs): ")

        elif n == '4':
            initial_state = State(int(n))
            initial_state.readStateFromFile("sudokuEasy.txt")

            print("Initial state: \n")
            print(initial_state.toString())

            option = input("Enter game method (bfs / gbfs): ")
        else:
            print("Not a valid number.")

        if (option == "bfs"):
            bfsGame = BFS(initial_state)

            final_state = bfsGame.solve()
        else:
            gbfsGame = GBFS(initial_state)
            gbfsGame.initialiseValueLists()

            final_state = gbfsGame.solve()

        if final_state != None:
            print("Final state: \n")
            print(final_state.toString())

        else:
            print("No solution was found")


Main = main()
Main.run()