class Product:
    def __init__(self, product_id : str, chilled : bool = False, hazardous : bool = False):
        self.product_id = product_id.lower()
        self.chilled = chilled
        self.hazardous = hazardous

        def __repr__(self):
            return f"<Product id={self.product.id}, chilled={self.chilled}, hazardous ={self.hazardous}>"