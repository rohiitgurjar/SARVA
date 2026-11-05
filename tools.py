from datetime import datetime #to use datetime.now() , we need to import this module
import requests

def get_current_time():
    return datetime.now().strftime("%Y-%M-%D %H-%M-%S") #this is pythons built-in feature for datetime;

def get_city_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url,timeout=10)
    return response.text

#TOOLS = [{},{},{}]

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description":"Returns the current time and date as a formatted string",
            "parameters":{"type":"object", "properties": {}},
        },
    },
    {
        "type":"function",
        "function": {
            "name":"get_city_weather",
            "description":"Returns teh current weather of a given city.",
            "parameters": {
                "type":"object",
                "properties":{
                    "city":{
                        "type":"string",
                        "description":"City to get the weather for."
                    }
                }
            }
        }
    }
]

FUNCTION_NAME_TO_FUNCTION_MAP = {
    "get_current_time": get_current_time,
    "get_city_weather": get_city_weather,
}