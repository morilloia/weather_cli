import requests, argparse
from collections import Counter
def check_request(url, params): # A function that checks the response from the API and handles any errors that may occur during the request
    try:
        r = requests.get(url, params=params, timeout=6)
        r.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        return r
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.reason}")
        exit()
    except requests.exceptions.ConnectionError as e:
        print("Error connecting to the API. Please check your internet connection and try again.")
        exit()
    except requests.exceptions.Timeout as e:
        print("Request timed out. Please try again later.")
        exit()
if __name__ == "__main__":

    #Defines a dictionary that maps weather codes to their corresponding weather descriptions
    weather_code_mapping = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        56: "Light freezing drizzle",
        57: "Dense freezing drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        66: "Light freezing rain",
        67: "Heavy freezing rain",
        71: "Slight snowfall",
        73: "Moderate snowfall",
        75: "Heavy snowfall",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        97: "Heavy thunderstorm",
        99: "Thunderstorm with heavy hail"
    }
    #Emojis for better visualization
    weather_emoji_mapping = {
    0: "☀️",   # Clear sky
    1: "🌤️",   # Mainly clear
    2: "⛅",   # Partly cloudy
    3: "☁️",   # Overcast
    45: "🌫️",  # Fog
    48: "🌫️",  # Depositing rime fog
    51: "🌦️",  # Light drizzle
    53: "🌦️",  # Moderate drizzle
    55: "🌦️",  # Dense drizzle
    56: "🌧️",  # Light freezing drizzle
    57: "🌧️",  # Dense freezing drizzle
    61: "🌧️",  # Slight rain
    63: "🌧️",  # Moderate rain
    65: "🌧️",  # Heavy rain
    66: "🌧️",  # Light freezing rain
    67: "🌧️",  # Heavy freezing rain
    71: "🌨️",  # Slight snowfall
    73: "🌨️",  # Moderate snowfall
    75: "❄️",   # Heavy snowfall
    77: "❄️",   # Snow grains
    80: "🌦️",  # Slight rain showers
    81: "🌧️",  # Moderate rain showers
    82: "⛈️",   # Violent rain showers
    85: "🌨️",  # Slight snow showers
    86: "❄️",   # Heavy snow showers
    95: "⛈️",   # Thunderstorm
    96: "⛈️",   # Thunderstorm with slight hail
    97: "⛈️",   # Heavy thunderstorm
    99: "⛈️",   # Thunderstorm with heavy hail
}
    #Sets up the argument parser to get the arguments directly from the command line
    parser = argparse.ArgumentParser(description='Get weather data from various ranges.',)
    parser.add_argument('city', type=str, help='City name to get weather data for',)
    parser.add_argument('--days', type=int, default=7, help='Number of days to get weather data for (default: 7)')
    args = parser.parse_args()
    try:
        location_url = 'https://geocoding-api.open-meteo.com/v1/search'
        r_location = check_request(location_url, {'name': args.city})
        location_data = r_location.json()

    except KeyError:
        print("City not found. Please check the city name and try again.")
        exit()
    #Defines the parameters based on the city name and the number of days specified in the command line arguments
    parameters = {
        "latitude": location_data['results'][0]['latitude'],
        "longitude": location_data['results'][0]['longitude'],
        "forecast_days": args.days,
        "hourly": "temperature_2m,weather_code",
    }
    url = "https://api.open-meteo.com/v1/forecast"
    r = check_request(url, parameters)


    #Turn the response from the API into a JSON object
    json_data = r.json()
    #Creates a dictionary to store the separated data by date
    separated = {}
    #Associates the hourly data from the JSON response with the corresponding date, temperature, and weather code
    combined_data = zip(json_data['hourly']['time'], json_data['hourly']['temperature_2m'], json_data['hourly']['weather_code'])
    for i in combined_data:
        #Splits the date and time from the timestamp and organizes the data into a dictionary with dates as keys and lists of temperatures and weather codes as values
        splitted = i[0].split("T")
        if splitted[0] not in separated:
            separated[splitted[0]] = [[], []]
        separated[splitted[0]][0].append(i[1])
        separated[splitted[0]][1].append(i[2])
    print(f"Weather forecast for {args.city}, {location_data['results'][0]['country_code']} for the next {args.days} days:\n")
    for key in separated.items():
        average_temp = sum(key[1][0]) / len(key[1][0])
        average_weather = Counter(key[1][1]).most_common(1)[0][0]
        print(f"📅 Date: {key[0]}, \n   Weather: {weather_emoji_mapping[average_weather]}  {weather_code_mapping[average_weather]},\n 🌡️  Avg temp: {average_temp:.2f}°C,\n ⬆️  Max temp: {max(key[1][0]):.2f}°C,\n ⬇️  Min temp: {min(key[1][0]):.2f}°C")


    




