from fastapi import FastAPI

app = FastAPI()

# Mock Database
hotels = {"1": {"name": "Grand Plaza", "rooms": 5, "price": 200}}


@app.get("/rooms")
def get_rooms():
    return hotels


@app.post("/book")
def book_room(hotel_id: str):
    if hotels[hotel_id]["rooms"] > 0:
        hotels[hotel_id]["rooms"] -= 1
        return {"status": "success", "message": f"Booked {hotels[hotel_id]['name']}"}
    return {"status": "error", "message": "No rooms left"}