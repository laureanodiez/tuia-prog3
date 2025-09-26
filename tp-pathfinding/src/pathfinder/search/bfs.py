from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state

        reached = {}
        reached[root.state] = True
        
        if grid.objective_test(root.state):
            return Solution(root, reached

                    )
        # Initialize frontier with the root node

        frontera = QueueFrontier()
        frontera.add

        # TODO Complete the rest!!
        # ...
        if frontera.is_empty()
            return NoSolution(root, reached)

        nodo = frontera.remove 

        for acciones in grid.actions(nodo.state)
            sucesor = grid.actions(nodo.state, acciones)
