// Create the map centered on your operational area
const map = L.map('map').setView([12.956, 77.664], 12);

// Tell Leaflet where to get the tiles
L.tileLayer('http://127.0.0.1:5000/tile/{z}/{x}/{y}', {

    minZoom: 10,
    maxZoom: 16,

    tileSize: 256,

    attribution: "Offline Map"

}).addTo(map);