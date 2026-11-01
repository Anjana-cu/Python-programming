import json
import pandas as pd

data = '''
{
    "cities": [
        {"city": "Kochi", "temperature": 30, "humidity": 75},
        {"city": "Chennai", "temperature": 35, "humidity": 60},
        {"city": "Delhi", "temperature": 28, "humidity": 50}
    ]
}
'''

weather = json.loads(data)

df = pd.DataFrame(weather["cities"])

print("Weather Report:")
print(df)

print("\nAverage Temperature:", df["temperature"].mean())
print("Average Humidity:", df["humidity"].mean())

print("\nCity-wise Weather:")

for city in weather["cities"]:
    print("\nCity:", city["city"])
    print("Temperature:", city["temperature"], "C")
    print("Humidity:", city["humidity"], "%")