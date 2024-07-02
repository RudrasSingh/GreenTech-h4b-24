document.addEventListener('DOMContentLoaded', function() {
    // Data for charts
    const energySavedData = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'Energy Saved (kWh)',
            data: [120, 150, 180, 200, 230, 260, 300],
            borderColor: 'rgba(40, 167, 69, 1)',
            backgroundColor: 'rgba(40, 167, 69, 0.2)',
            fill: true,
            tension: 0.4
        }]
    };

    const co2ReducedData = {
        labels: ['Project A', 'Project B', 'Project C', 'Project D'],
        datasets: [{
            label: 'CO2 Reduced (tons)',
            data: [10, 15, 8, 12],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)'
            ],
            borderWidth: 1
        }]
    };

    // Config for charts
    const energySavedConfig = {
        type: 'line',
        data: energySavedData,
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Energy Saved Over Time'
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        },
    };

    const co2ReducedConfig = {
        type: 'bar',
        data: co2ReducedData,
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'CO2 Emissions Reduced'
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        },
    };

    // Initialize charts
    const energySavedChart = new Chart(
        document.getElementById('energySavedChart'),
        energySavedConfig
    );

    const co2ReducedChart = new Chart(
        document.getElementById('co2ReducedChart'),
        co2ReducedConfig
    );

    // Simulated real-time data updates
    function updateRealTimeData() {
        const energyProduction = Math.floor(Math.random() * 1000);
        const co2Emissions = (Math.random() * 100).toFixed(2);

        document.getElementById('energyProduction').textContent = `${energyProduction} kW`;
        document.getElementById('co2Emissions').textContent = `${co2Emissions} tons`;
    }

    // Update real-time data every 5 seconds
    setInterval(updateRealTimeData, 5000);
    updateRealTimeData(); // Initial call to display data immediately
});
