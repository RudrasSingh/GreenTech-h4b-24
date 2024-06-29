from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Function to fetch emissions factors based on location
def get_emissions_factors(lat, lon):
    # For simplicity, this example uses a static dictionary. In a real implementation,
    # you would use an API to get region-specific emissions factors.
    region_emissions = {
        'default': {
            'electricity': 0.82,
            'transport': 0.2,
            'cooking': 2.98
        }
    }
    # Here you could call an external API to get actual data based on lat and lon
    # For example:
    # response = requests.get(f'http://api.example.com/emissions?lat={lat}&lon={lon}')
    # data = response.json()
    # return data['emissions_factors']

    # Return default emissions factors for this example
    return region_emissions['default']

@app.route('/api/calculate-carbon-footprint', methods=['POST'])
def calculate_carbon_footprint():
    data = request.json
    lat = data['latitude']
    lon = data['longitude']
    
    # Fetch emissions factors based on location
    emissions_factors = get_emissions_factors(lat, lon)
    
    # Example user data, in a real scenario this should be dynamically fetched
    user_data = {
        'electricity': 100,  # kWh
        'transport': 50,     # km
        'cooking': 10        # kg LPG
    }
    
    footprint = (
        user_data['electricity'] * emissions_factors['electricity'] +
        user_data['transport'] * emissions_factors['transport'] +
        user_data['cooking'] * emissions_factors['cooking']
    )
    
    return jsonify({'footprint': footprint}), 200

if __name__ == '__main__':
    app.run(debug=True)
