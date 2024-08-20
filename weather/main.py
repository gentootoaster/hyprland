import python_weather
import asyncio
import os

async def getweather():
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        # fetch a weather forecast from a city
        weather = await client.get('Tyumen') 

        # check the kind attribute to determine the weather condition
        if weather.kind == python_weather.enums.Kind.SUNNY:
            icon = " "
        elif weather.kind == python_weather.enums.Kind.CLOUDY:
            icon = " "
        elif weather.kind == python_weather.enums.Kind.PARTLY_CLOUDY:
            icon = " "
        elif weather.kind == python_weather.enums.Kind.FOG:
            icon = " "
        elif weather.kind == python_weather.enums.Kind.LIGHT_RAIN or weather.kind == python_weather.enums.Kind.LIGHT_SHOWERS:
            icon = " "
        elif weather.kind == python_weather.enums.Kind.HEAVY_RAIN or weather.kind == python_weather.enums.Kind.HEAVY_SHOWERS:
            icon = " "
        elif weather.kind == python_weather.enums.Kind.LIGHT_SNOW or weather.kind == python_weather.enums.Kind.LIGHT_SNOW_SHOWERS:
            icon = " "
        elif weather.kind == python_weather.enums.Kind.HEAVY_SNOW or weather.kind == python_weather.enums.Kind.HEAVY_SNOW_SHOWERS:
            icon = " "
        elif weather.kind == python_weather.enums.Kind.LIGHT_SLEET or weather.kind == python_weather.enums.Kind.LIGHT_SLEET_SHOWERS:
            icon = " "
        elif weather.kind == python_weather.enums.Kind.THUNDERY_HEAVY_RAIN or weather.kind == python_weather.enums.Kind.THUNDERY_SHOWERS:
            icon = " "
        elif weather.kind == python_weather.enums.Kind.THUNDERY_SNOW_SHOWERS:
            icon = " "
        elif weather.kind == python_weather.enums.Kind.VERY_CLOUDY:
            icon = " " 
        else:
            icon = ""  # Unknown weather condition
        
        print(f"{weather.temperature}°C {icon}")

if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    asyncio.run(getweather())
