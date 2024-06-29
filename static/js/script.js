// script.js
document.addEventListener('DOMContentLoaded', (event) => {
    getLocation();
});

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, useDefaultPosition);
    } else {
        useDefaultPosition();
    }
}

function showPosition(position) {
    const latitude = position.coords.latitude.toFixed(2);
    const longitude = position.coords.longitude.toFixed(2);

    document.getElementById('coordinates').innerHTML = `Latitude: ${latitude} <br> Longitude: ${longitude}`;

    // Call the function to get weather data
    getWeatherData(latitude, longitude);
}

function useDefaultPosition() {
    const latitude = 34.22;
    const longitude = 88.22;

    document.getElementById('coordinates').innerHTML = `Latitude: ${latitude} <br> Longitude: ${longitude}`;

    // Call the function to get weather data
    getWeatherData(latitude, longitude);
}

function getWeatherData(lat, lon) {
    const data = null;

    const xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener('readystatechange', function () {
        if (this.readyState === this.DONE) {
            const response = JSON.parse(this.responseText);

            // Extract the necessary data
            const locationName = response.location.name;
            const temp_c = response.current.temp_c;
            const humidity = response.current.humidity;
            const icon = `https:${response.current.condition.icon}`;
            const conditionText = response.current.condition.text;

            // Update the HTML with the extracted data
            document.getElementById('location-name').innerText = locationName;
            document.getElementById('temp_c').innerText = temp_c;
            document.getElementById('humidity').innerText = humidity;
            document.getElementById('icon').src = icon;
            document.getElementById('condition-text').innerText = conditionText;
        }
    });

    const url = `https://weatherapi-com.p.rapidapi.com/current.json?q=${lat}%2C${lon}`;
    xhr.open('GET', url);
    xhr.setRequestHeader('x-rapidapi-key', '61edba90famsha86f9cf13c233a7p10921ejsn6156531a5740');
    xhr.setRequestHeader('x-rapidapi-host', 'weatherapi-com.p.rapidapi.com');

    xhr.send(data);
}



