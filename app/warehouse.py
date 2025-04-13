from app.cell import Cell
from app.product import Product

class Warehouse:
    def __init__(self):
        self.rows = 10
        self.cols = 10
        self.shelves = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self._init_cells()

    def _init_cells(self):
        for x in range(self.rows):
            for y in range(self.cols):
                if x >= 7 and y >= 6:
                    self.shelves[x][y] = Cell(x, y, has_cooling=True, is_hazardous=True)
                elif x >= 7:
                    self.shelves[x][y] = Cell(x, y, has_cooling=True)
                elif y == 9:
                    self.shelves[x][y] = Cell(x, y, is_hazardous=True)
                else:
                    self.shelves[x][y] = Cell(x, y)

    def allocate_cell(self, product: Product, quantity: int) -> dict:
        if quantity <= 0 or quantity > 10:
            return {"foundCell": False, "reason": "Invalid quantity"}

        preferred_order = [
            (0, 0), (0, 2), (0, 9), (1, 9),
            (7, 0), (7, 6), (7, 7), (7, 9)
        ]

        for x, y in preferred_order:
            cell = self.shelves[x][y]
            if cell.can_store(product, quantity):
                cell.store(product, quantity)
                return {"foundCell": True, "cell": f"{x},{y}"}

        return {"foundCell": False, "reason": "No suitable cell found"}
