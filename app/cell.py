from app.product import Product

class Cell: 
    def __init__(self, x: int, y: int, has_cooling=False, is_hazardous=False):
        self.x = x
        self.y = y
        self.has_cooling = has_cooling
        self.is_hazardous = is_hazardous
        self.capacity = 10
        self.product : Product | None = None
        self.quantity = 0

        def can_store(self, product : Product, quantity: int) -> bool:
            if self.capacity < quantity:
                return False
            if self.product and self.product.product_id != product.product_id:
                return False
            if product.hazardous and not self.is_hazardous: 
                return False
            return True
        
        def store(self,product:Product, quantity : int):
            if not self.can_store(product, quantity):
                raise ValueError(f"Cannot store product {product.product_id} in cell ({self.x}, {self.y})")
            if self.product is None:
                self.product = product
            self.quantity += quantity
            self.capacity -= quantity

        def __repr__(self):
            return f"Cell ({self.x}, {self.y}) {self.quantity}*{self.product.product_id if self.profuct else 'empty'}"