// Fetch safest route via Google Maps API
const response = await fetch(
    `https://maps.googleapis.com/maps/api/directions/json?origin=CapeTown&destination=Johannesburg&avoid=snow&key=API_KEY`
  );
  const data = await response.json();
  console.log(data.routes[0].warnings); // Alerts for N3 road closures