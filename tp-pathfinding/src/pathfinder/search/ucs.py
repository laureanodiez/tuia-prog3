from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        frontera = PriorityQueueFrontier()
        frontera.add(root, root.cost)
        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        while True:
                # Si la frontera está vacía, no hay solución
                if frontera.is_empty():
                    return NoSolution(reached)

                #  Extraer el nodo con menor costo acumulado
                nodo = frontera.pop()

                #  Verificar si este nodo alcanza el objetivo
                if grid.objective_test(nodo.state):
                    return Solution(nodo, reached)

                #  Expandir los sucesores
                for accion in grid.actions(nodo.state):
                    sucesor = grid.result(nodo.state, accion)
                    nuevo_costo = nodo.cost + grid.individual_cost(nodo.state, accion)

                    #  Si no fue alcanzado o encontramos un costo menor
                    if sucesor not in reached or nuevo_costo < reached[sucesor]:
                        # Crear nuevo nodo hijo
                        Nhijo = Node("", sucesor, nuevo_costo, nodo, accion)

                        # Actualizar costo alcanzado
                        reached[sucesor] = nuevo_costo

                        # Añadir a la frontera con su costo como prioridad
                        frontera.add(Nhijo, nuevo_costo)    

            # Initialize frontier with the root node
            # TODO Complete the rest!!
            # ...

        return NoSolution(reached)
