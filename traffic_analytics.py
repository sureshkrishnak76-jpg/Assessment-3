# Smart City Traffic Analytics System

junctions = [
    {
        "Junction ID": "J101",
        "Vehicle Count": 1200,
        "Average Speed": 40,
        "Accident Count": 5,
        "Signal Delay": 60,
        "Pollution Index": 180,
        "Peak Hour Traffic": 1500
    },
    {
        "Junction ID": "J102",
        "Vehicle Count": 900,
        "Average Speed": 35,
        "Accident Count": 2,
        "Signal Delay": 40,
        "Pollution Index": 120,
        "Peak Hour Traffic": 1100
    },
    {
        "Junction ID": "J103",
        "Vehicle Count": 1500,
        "Average Speed": 30,
        "Accident Count": 7,
        "Signal Delay": 80,
        "Pollution Index": 220,
        "Peak Hour Traffic": 1800
    },
    {
        "Junction ID": "J104",
        "Vehicle Count": 700,
        "Average Speed": 45,
        "Accident Count": 1,
        "Signal Delay": 25,
        "Pollution Index": 90,
        "Peak Hour Traffic": 800
    },
    {
        "Junction ID": "J105",
        "Vehicle Count": 1300,
        "Average Speed": 32,
        "Accident Count": 6,
        "Signal Delay": 70,
        "Pollution Index": 200,
        "Peak Hour Traffic": 1600
    }
]

print("=" * 120)
print("SMART CITY TRAFFIC ANALYTICS SYSTEM")
print("=" * 120)

# 1. Calculate Congestion Score
for j in junctions:
    j["Congestion Score"] = round(
        (j["Vehicle Count"] * j["Signal Delay"]) /
        j["Average Speed"], 2
    )

# Display Junction Details
print("\nJunction Details")
print("-" * 120)
print(f'{"ID":<10}{"Vehicles":<12}{"Speed":<10}{"Delay":<10}{"Congestion":<15}{"Pollution":<12}')
print("-" * 120)

for j in junctions:
    print(f'{j["Junction ID"]:<10}'
          f'{j["Vehicle Count"]:<12}'
          f'{j["Average Speed"]:<10}'
          f'{j["Signal Delay"]:<10}'
          f'{j["Congestion Score"]:<15}'
          f'{j["Pollution Index"]:<12}')

print("-" * 120)

# 2. Rank Junctions
junctions.sort(key=lambda x: x["Congestion Score"], reverse=True)

print("\n2. Junction Ranking")
print("-" * 35)
print(f'{"Rank":<8}{"Junction":<12}{"Score":<12}')
print("-" * 35)

for i, j in enumerate(junctions, start=1):
    j["Rank"] = i
    print(f'{i:<8}{j["Junction ID"]:<12}{j["Congestion Score"]:<12}')

print("-" * 35)

# 3. Accident-Prone Areas
print("\n3. Accident-Prone Junctions")

for j in junctions:
    if j["Accident Count"] >= 5:
        print(j["Junction ID"], "- Accidents:", j["Accident Count"])

# 4. Heavily Polluted Junctions
print("\n4. Heavily Polluted Junctions")

for j in junctions:
    if j["Pollution Index"] > 150:
        print(j["Junction ID"], "- Pollution:", j["Pollution Index"])

# 5. City Average Congestion
average = sum(j["Congestion Score"] for j in junctions) / len(junctions)

print("\n5. City Average Congestion")
print(round(average, 2))

# 6. Busiest Junction
busiest = max(junctions, key=lambda x: x["Peak Hour Traffic"])

print("\n6. Busiest Junction")
print("Junction :", busiest["Junction ID"])
print("Peak Traffic :", busiest["Peak Hour Traffic"])

# 7. Generate Traffic Alerts
print("\n7. Traffic Alerts")

alerts = []

for j in junctions:
    if j["Congestion Score"] > average:
        alert = f'ALERT: {j["Junction ID"]} is highly congested.'
        alerts.append(alert)
        print(alert)

# 8. Save Alerts to File
with open("traffic_alerts.txt", "w") as file:
    for alert in alerts:
        file.write(alert + "\n")

print("\nAlerts saved successfully.")

# 9. Sort Junctions by Vehicle Count
junctions.sort(key=lambda x: x["Vehicle Count"], reverse=True)

print("\n9. Junctions Sorted by Vehicle Count")
print("-" * 35)
print(f'{"Junction":<15}{"Vehicles":<15}')
print("-" * 35)

for j in junctions:
    print(f'{j["Junction ID"]:<15}{j["Vehicle Count"]:<15}')

print("-" * 35)

# 10. Display Top 5 Congestion Points
junctions.sort(key=lambda x: x["Congestion Score"], reverse=True)

print("\n10. Top 5 Congestion Points")
print("-" * 40)
print(f'{"Junction":<15}{"Congestion":<15}')
print("-" * 40)

for j in junctions[:5]:
    print(f'{j["Junction ID"]:<15}{j["Congestion Score"]:<15}')

print("-" * 40)

# Read Alerts File
print("\nTraffic Alerts File")
with open("traffic_alerts.txt", "r") as file:
    print(file.read())

print("=" * 120)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 120)