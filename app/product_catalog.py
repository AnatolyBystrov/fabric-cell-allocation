from app.product import Product


product_catalog = {
    "bread": Product("bread"),
    "bamba": Product("bamba"),
    "apple": Product("apple"),
    "pasta": Product("pasta"),
    "salt": Product("salt"),
    "yogourt": Product("yogourt", chilled=True),
    "milk": Product("milk", chilled=True),
    "cheese": Product("cheese", chilled=True),
    "insulin": Product("insulin", chilled=True, hazardous=True),
    "bleach": Product("bleach", hazardous=True),
    "stain removal": Product("stain removal", hazardous=True),
}


def get_product(name: str) -> Product:
    """
    Возвращает объект Product по имени, либо None, если не найден.
    """
    return product_catalog.get(name.lower())
