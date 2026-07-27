// Create the map centered on your operational area
const map = L.map('map').setView([12.956, 77.664], 16);

// Tell Leaflet where to get the tiles
L.tileLayer('http://127.0.0.1:5000/tile/{z}/{x}/{y}', {

     minZoom: 10,
     maxZoom: 19,       // Allow user to zoom to 19
     maxNativeZoom: 16, // Tiles only exist up to zoom 16
    tileSize: 256,
    attribution: "Offline Map"

}).addTo(map);
let vehicleMarker = L.marker([12.966883, 77.700300]).addTo(map);

let pathCoordinates = [];

vehicleMarker.bindPopup("Vehicle");

let trajectory = L.polyline([], {
    color: "blue",
    weight: 5,
    opacity: 1
}).addTo(map);

async function updateVehicle() {

    const response = await fetch("/telemetry");

    const data = await response.json();


    vehicleMarker.setLatLng([
        data.latitude,
        data.longitude
    ]);
    pathCoordinates.push([
    data.latitude,
    data.longitude
]);

trajectory.setLatLngs(pathCoordinates);

    map.panTo([
        data.latitude,
        data.longitude
    ]);
document.getElementById("time").textContent = data.time;

document.getElementById("latitude").textContent =
    data.latitude.toFixed(6);

document.getElementById("longitude").textContent =
    data.longitude.toFixed(6);

document.getElementById("altitude").textContent =
    data.altitude + " m";

document.getElementById("source").textContent =
    data.source;

document.getElementById("destination").textContent =
    data.destination;
}

// First update immediately
updateVehicle();

// Update every 10 seconds
setInterval(updateVehicle, 10000);