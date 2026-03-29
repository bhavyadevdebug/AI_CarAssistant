import requests

def get_vehicle_info(vin: str) -> dict:
    """
    Fetch vehicle data for a given VIN using NHTSA's VIN decoder API.
    Returns structured info (make, model, year, etc.).
    """
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/{vin}?format=json"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Failed to fetch VIN data"}

    data = response.json()

    if "Results" not in data or len(data["Results"]) == 0:
        return {"error": "Invalid VIN response"}

    vehicle_info = data["Results"][0]

    return {
        "make": vehicle_info.get("Make"),
        "model": vehicle_info.get("Model"),
        "model_year": vehicle_info.get("ModelYear"),
        "manufacturer": vehicle_info.get("Manufacturer"),
        "recalls_check_note": "Use NHTSA recall endpoint for recall data"
    }