
# import requests

# def show_weather():
#     API_KEY = "f35231d22a4478c49fdf18398b134507"
#     CITY = input("enter city name: ")
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
#     try: 
#         response = requests.get(url)
#         if response.status_code == 200:
#             data = response.json()
#             temperature = data["main"]["temp"]
#             weather_desc = data['weather'][0]['description']
#             humidity = data['main']['humidity']
#             print(f" -----the weather of : {CITY} ----")
#             print(f"temperature: {temperature}°C")
#             print(f"weather_desc : {weather_desc.capitalize()}")
#             print(f"humidity: {humidity}%")
#         else:
#             print(f"Error, check it please: {response.status_code}")
#             print("please check your API_KEY nad CITY name")

#     except Exception as e:
#         print("error:", e)
# while True:
#     print("\n---")
#     print("1. show weather")

#     choice = input("enter choice: ")
#     if choice == "1":
#         show_weather()
