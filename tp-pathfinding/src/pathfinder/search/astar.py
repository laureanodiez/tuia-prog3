from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Inicializar la heurística con el estado inicial y el objetivo final
        h = AStarSearch.h(root.state, grid.end)
        frontera = PriorityQueueFrontier()
        # Añadir el costo de la heurística
        frontera.add(root, root.cost+h)
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
                        # Actualizar la heurística
                        h_act = AStarSearch.h(sucesor, grid.end)

                        # Añadir a la frontera contemplando la heurística actualizada
                        frontera.add(Nhijo, nuevo_costo+h_act)    

        return NoSolution(reached)
    
    def h(state, end)->int:
        """Implementación de Heurística: Calcula la distancia Manhattan entre dos puntos
        
        Args:
            state: Estado actual (tupla con coordenadas x, y)
            end: Estado objetivo (tupla con coordenadas x, y)
            
        Returns:
            int: Distancia Manhattan
        """
        return abs(state[0] - end[0]) + abs(state[1] - end[1])
        