from fastapi import FastAPI
from pymongo import MongoClient
from app.warehouse import Warehouse
from app.product_catalog import get_product
from fastapi import HTTPException

app = FastAPI()

client = MongoClient("mongodb://mongo:27017")
db = client["allocator_db"]
allocations = db["allocations"]

warehouse = Warehouse()

@app.get("/")
def root():
    return{"message":"Fabric Cell Allocator API is running"}

@app.post("/allocate")
def allocate(product_name: str, quantity: int):
    product = get_product(product_name)
    result = warehouse.find_cell_for_product(product, quantity)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    allocation_data = {
        "product": product_name,
        "quantity": quantity,
        "cell": result["cell"]
    }
    allocations.insert_one(allocation_data)

    return{
        "message": "Product allocated succesfully",
        "cell": result["cell"]
    }