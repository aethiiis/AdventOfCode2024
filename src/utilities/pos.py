class Pos:
    x:int
    y:int

    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"(x = {self.x}, y = {self.y})"

    def __eq__(self, __o: object) -> bool:
        return type(__o) == type(self) and __o.x == self.x and __o.y == self.y
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def manhattan_dist(self, other) -> int:
        if type(self) == type(other):
            return abs(self.x - other.y) + abs(self.y - other.y)
        else:
            return -1