from pos import Pos

class Graph:
    grid:dict[Pos, int]

    def __init__(self, grid:dict[Pos, int] = None, dim:tuple[int, int, int, int] = None, default_value = 0) -> None:
        if grid:
            self.grid = grid
        elif dim:
            xmin:int = dim[0]
            xmax:int = dim[1]
            ymin:int = dim[2]
            ymax:int = dim[3]

            for i in range(xmin, xmax+1):
                for j in range(ymin, ymax+1):
                    pos = Pos(i, j)
                    self.grid[pos] = default_value

    def __str__(self) -> str:
        liste:list = self.to_list()
        string:str = ""

        for i in range(len(liste)):
            for j in range(len(liste[i])):
                string += liste[i][j]
            string += "\n"

        return string

    def __repr__(self) -> str:
        liste:list = self.to_list()
        string:str = ""

        for i in range(len(liste)):
            for j in range(len(liste[i])):
                string += liste[i][j]
            string += "\n"

        return string

    def __eq__(self, __o: object) -> bool:
        return self.included_in(__o) and self.contains(__o)
    
    def included_in(self, __o:object) -> bool:
        if type(self) != type(__o):
            return False
        
        for key, value in self.grid.items():
            if __o.grid.get(key) != value:
                return False
        
        return True
    
    def contains(self, __o:object) -> bool:
        if type(self) != type(__o):
            return False
        
        for key, value in __o.grid.items():
            if self.grid.get(key) != value:
                return False
        
        return True
    
    def get_dim(self) -> tuple[int, int, int, int]:
        positions:list = self.grid.keys()
        
        xmin:int = positions[0].x
        xmax:int = positions[-1].x
        ymin:int = positions[0].y
        ymax:int = positions[-1].y

        for pos in positions:
            if pos.x < xmin:
                xmin = pos.x
            elif pos.x > xmax:
                xmax = pos.x
            elif pos.y < ymin:
                ymin = pos.y
            elif pos.y > ymax:
                ymax = pos.y
        
        return (xmin, xmax, ymin, ymax)

    def to_list(self):
        xmin, xmax, ymin, ymax = self.get_dim()

        return [[self.grid.get(Pos(i, j), 0) for i in range(xmax-xmin+1)] for j in range(ymax-ymin+1)]
    
    def neighbors(self, element:Pos) -> list[Pos]:
        l:list[Pos] = []
        dims:tuple = self.get_dim()

        xmin = dims[0]
        xmax = dims[1]
        ymin = dims[2]
        ymax = dims[3]

        up:Pos = Pos(x = element.x, y = element.y - 1)
        down:Pos = Pos(x = element.x, y = element.y + 1)
        left:Pos = Pos(x = element.x - 1, y = element.y)
        right:Pos = Pos(x = element.x + 1, y = element.y)

        if up.x >= xmin and up.x <= xmax and up.y >= ymin and up.y <= ymax:
            l.append(up)
        if down.x >= xmin and down.x <= xmax and down.y >= ymin and down.y <= ymax:
            l.append(down)
        if left.x >= xmin and left.x <= xmax and left.y >= ymin and left.y <= ymax:
            l.append(left)
        if right.x >= xmin and right.x <= xmax and right.y >= ymin and right.y <= ymax:
            l.append(right)
        
        return l