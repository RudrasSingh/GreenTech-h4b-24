def calculate_carbon_footprint(electricity_kWh, fuel_liters, waste_kg, flight_hours,region):
    # Conversion factors for different regions (example values)
    region_factors = {
        "default": {"electricity_factor": 0.92, "fuel_factor": 2.31, "waste_factor": 0.5, "flight_factor": 0.25},
        "india": {"electricity_factor": 0.82, "fuel_factor": 2.35, "waste_factor": 0.45, "flight_factor": 0.3},
        "us": {"electricity_factor": 0.45, "fuel_factor": 2.31, "waste_factor": 0.55, "flight_factor": 0.22},
        # Add more regions as needed
    }
    
    # Get conversion factors for the specified region
    factors = region_factors.get(region, region_factors["default"])
    
    # Calculate individual carbon footprints
    electricity_footprint = electricity_kWh * factors["electricity_factor"]
    fuel_footprint = fuel_liters * factors["fuel_factor"]
    waste_footprint = waste_kg * factors["waste_factor"]
    flights_footprint = flight_hours * factors["flight_factor"]
    
    # Sum the carbon footprints
    total_footprint = electricity_footprint + fuel_footprint + waste_footprint + flights_footprint
    
    return total_footprint

# Example usage
# electricity_kWh = 100    # Monthly electricity consumption in kWh
# fuel_liters = 50         # Monthly fuel consumption in liters
# waste_kg = 20            # Monthly waste production in kg
# flight_hours = 5         # Monthly flight hours
# region = "india"         # Specify the region

# total_carbon_footprint = calculate_carbon_footprint(electricity_kWh, fuel_liters, waste_kg, flight_hours, region)
# print(f"Total Carbon Footprint: {total_carbon_footprint} kg CO2e")
