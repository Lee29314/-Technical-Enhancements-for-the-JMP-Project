def calculate_co2(distance_km, vehicle_type):
    # Emissions in kg CO2 per km (source: EPA)
    emissions = {
        "petrol_car": 0.192,
        "hybrid": 0.105,
        "electric": 0.053
    }
    return distance_km * emissions.get(vehicle_type, 0.15)