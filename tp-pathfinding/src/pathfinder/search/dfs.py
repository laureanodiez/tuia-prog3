from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        # Initialize explored with the initial state
        explored = {}

        if grid.objective_test(root.state):
            return Solution(root, explored)
        frontera = StackFrontier()
        frontera.add(root)

        # Initialize frontier with the root node
        # TODO Complete the rest!!
        # ...
        
        while True: 
            if frontera.is_empty():
                print("frontera vacia")
                return NoSolution(explored)

            nodo = frontera.remove()
            if nodo.state in explored: 
                print("nodostate en explorados")
                continue
            explored[nodo.state] = True
            for accion in grid.actions(nodo.state):
                print("iteracion del for")
                sucesor = grid.result(nodo.state, accion)
                if sucesor not in explored:
                    print("sucesor sin explorar")
                    Nhijo = Node("", sucesor, nodo.cost + grid.individual_cost(nodo.state, accion), nodo, accion)
                    if grid.objective_test(sucesor):
                        print("si el hijo es ot, solution")
                        return Solution(Nhijo, explored)
                    frontera.add(Nhijo)
