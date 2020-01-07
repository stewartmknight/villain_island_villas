// Create a map object
var myMap = L.map("map", {
  center: [15.5994, -28.6731],
  zoom: 3
});

L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.comic",
  accessToken: API_KEY
}).addTo(myMap);

// Country data
var countries = [
  {
    name: "South Pacific", 
    Island: "Fiji <p> Price: $25,000,000", 
    location: [32.28, -80.61],
    points: 1
  },
  {
    name: "Mexico", 
    Island: "Violin <p> Price: $18,000,000", 
    location: [32.28, -80.61],
    points: 1
  },
  {
    name: "South Pacific", 
    Island: "New Zealand <p> Price: $11,467,068", 
    location: [-36.79, 175.19],
    points: 1
  },
  {
    name: "Australia", 
    Island: "The Duke Group <p> Price: $11,379,153", 
    location: [-36.79, 175.19],
    points: 3
  },
  {
    name: "Bahamas", 
    Island: "Frozen Cay <p> Price: $29,000,000", 
    location: [24.21, -74.47],
    points: 2
  },
  {
    name: "Canada", 
    Island: "Breakwater <p> Price: $6,015,891", 
    location: [45.76, -80.64],
    points: 3
  },
  {
    name: "Brazil", 
    Island: "Bainema Paradise <p> Price: $4,680,000", 
    location: [-13.62, -38.90],
    points: 1
  },
  {
    name: "United States",
    Island: "St. Phillips <p> Price: $Sold", 
    location: [32.28, -80.61],
    points: 3
  },
  {
    name: "United States",
    Island: "Wiskey <p> Price: $2,950,000", 
    location: [44.24, -76.15],
    points: 3
  },
  {
    name: "Croatia",
    Island: "Trstenik <p> Price: $1,171,352", 
    location: [44.86, 14.76],
    points: 1
  },
  {
    name: "Australia",
    location: [-25.27, 133.77],
    rank: 13,
    points: 2
  },
  {
    name: "Norway",
    location: [60.25, 10.70],
    rank: 7,
    points:3
  },
  {
    name: "Greece",
    Island: "Patroklos <p> Price: $160_000_000", 
    location: [37.65, 23.94],
    points:1
  },
  {
    name: "Thailand",
    Island: "Rangyai <p> Price: $159_000_000", 
    location: [7.95, 98.44],
    points: 1
  },
  {
    name: "USA",
    Island: "Rangyai <p> Price: $95_000_000", 
    location: [24.71, -81.55],
    points: 2
  },
  {
    name: "Bahamas",
    Island: "The Exumas <p> Price: $62_000_000", 
    location: [24.71, -81.55],
    points: 1
  },
  {
    name: "Sudan",
    Island: "N/A",
    location:[12.86, 30.21],
    points: 1
  },
  {
    name: "Niger",
    Island: "N/A",
    location: [17.60, 8.081],
    points: 1
  },
  {
    name: "Peru",
    Island: "N/A",
    location: [9.19, 75.01],
    points: 1
  },
  {
    name: "Chile",
    Island: "N/A",
    location: [35.67, 71.54],
    points: 1
  },
  {
    name: "Russia",
    Island: "N/A",
    location: [61.52, 105.31],
    points: 1
  },
];


// Loop through the cities array and create one marker for each city object
for (var i = 0; i < countries.length; i++) {

  // Conditionals for countries points
  var color = "";
  if (countries[i].points >=3) {
    color = "green";
  }
  else if (countries[i].points >=2) {
    color = "yellow";
  }
  else if (countries[i].points >=1 ) {
    color = "red";
  }
  else {
    color = "gray";
  }

  // Add circles to map
  L.circle(countries[i].location, {
    fillOpacity: 0.75,
    color: "white",
    fillColor: color,
    // Adjust radius
    radius:  300000
  }).bindPopup("<h1>" + countries[i].name + "</h1> <hr> <h3>Island: " 
                      + countries[i].Island + "</h3> <hr> <h3>Points:"
                      + countries[i].points + "</h3>").addTo(myMap);
}
