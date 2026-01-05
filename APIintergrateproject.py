import requests
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
city = input("Enter city name:  ")
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}
try:
    response=requests.get(BASE_URL, params=params, timeout=10)
    if response.status_code == 200:
        data=response.json()
        city_name = data["name"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]
        print("Wheather report...")
        print("-"*30)
        print(f"City :{city_name}")
        print(f"Temperature :{temperature}oC")
        print(f"Feels_Like :{feels_like}")
        print(f"Humidity :{humidity}")
        print(f"Condition :{weather_desc.title()}")
        print(f"Wind_Speed :{wind_speed}m/s")
    elif response.status_code == 404:
        print("City not found. please check the name.")
    else:
        print("failed to fetch weather data.")
        print("Status code:", response.status_code)
except requests.exceptions.Timeout:
    print("your request timed out. please try again later.")
except Exception as e:
    print("your request was failed..",e)



