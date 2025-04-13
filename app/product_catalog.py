from app.product import Product

product_catalog ={
    "bread": Product("bread"),
    "bamba": Product("bamba"),
    "apple": Product("apple"),
    "pasta": Product("pasta"),
    "salt": Product("salt"),
    "yogourt": Product("yogourt", chilled=True),
    "milk": Product("milk", chilled=True),
    "cheese":Product("cheese", chilled=True),
    "insulin":Product("insulin",chilled=True, hazardous=True),
    "bleach":Product("bleach",hazardous=True),
    "stain removal": Product("stain remuval", hazardous=True),
}