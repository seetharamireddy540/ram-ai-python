from mcp.server.fastmcp import FastMCP

mcp = FastMCP("HotelBooking")

@mcp.tool()
async def check_hotel_availability() -> str:
    """Checks available hotels and pricing."""
    # In a real app, you'd fetch from the FastAPI service above
    return "Hotel 1: Grand Plaza - $200 (5 rooms available)"

@mcp.tool()
async def make_reservation(hotel_id: str) -> str:
    """Books a room at a specific hotel."""
    return f"Successfully booked hotel {hotel_id}!"