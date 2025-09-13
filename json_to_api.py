from fastapi import FastAPI, HTTPException

# === Hardcoded JSON Data ===
items = [
    {"id": 1, "name": "Apple", "price": 100},
    {"id": 2, "name": "Banana", "price": 40},
    {"id": 3, "name": "Mango", "price": 80},
]

# === FastAPI App ===
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome! Visit /items or /docs"}

@app.get("/items")
def get_items():
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(404, "Item not found")
