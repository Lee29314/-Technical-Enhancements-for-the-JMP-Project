import requests

def get_weather_alerts(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url).json()
    if "snow" in response["weather"][0]["description"].lower():
        return "⚠️ Snow Alert: Avoid travel or use 4x4!"
    return "Weather OK for travel."