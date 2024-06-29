const options = {
    method: 'GET',
    headers: {
        'x-rapidapi-key': '61edba90famsha86f9cf13c233a7p10921ejsn6156531a5740',
        'x-rapidapi-host': 'air-quality.p.rapidapi.com'
    }
};

async function fetchAirQuality() {
    try {
        const position = await getUserLocation();
        const url = `https://air-quality.p.rapidapi.com/current/airquality?lon=${position.coords.longitude}&lat=${position.coords.latitude}`;
        
        const response = await fetch(url, options);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        const data = await response.json();
        displayAirQuality(data);
    } catch (error) {
        console.error('Error fetching air quality data:', error);
    }
}

function getUserLocation() {
    return new Promise((resolve, reject) => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(resolve, reject);
        } else {
            reject(new Error('Geolocation is not supported by this browser.'));
        }
    });
}

function displayAirQuality(data) {
    document.getElementById('city-name').textContent = data.city_name;
    document.getElementById('aqi').textContent = data.data[0].aqi;
    document.getElementById('co').textContent = data.data[0].co.toFixed(2); // Display CO with two decimal places
    document.getElementById('no2').textContent = data.data[0].no2.toFixed(2); // Display NO2 with two decimal places
    document.getElementById('o3').textContent = data.data[0].o3.toFixed(2); // Display O3 with two decimal places
}

// Call fetchAirQuality to initiate the process
fetchAirQuality();
