from graph import Graph
from pos import Pos
from queue import PriorityQueue

def astar(graph:Graph, start:Pos, goal:Pos, start_cost:int = 0) -> tuple[dict[Pos, Pos], dict[Pos, int]]:
    frontier:PriorityQueue = PriorityQueue()
    frontier.put((start, start_cost))

    came_from:dict[Pos, Pos] = dict()
    cost_so_far:dict[Pos, int] = dict()

    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current[0] == goal:
            break

        for next in graph.neighbors(current[0]):
            new_cost:int = cost_so_far[current[0]] + graph.grid[next]
            
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + next.manhattan_dist(goal)
                frontier.put((next, priority))
                came_from[next] = current[0]
    
    return came_from, cost_so_far