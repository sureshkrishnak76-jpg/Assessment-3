# Industrial IoT Machine Performance Monitoring

machines = [
    {
        "Machine ID": 101,
        "Plant Name": "Plant A",
        "Operating Hours": 500,
        "Downtime": 20,
        "Energy Consumption": 2500,
        "Units Produced": 12000,
        "Maintenance Cost": 15000
    },
    {
        "Machine ID": 102,
        "Plant Name": "Plant B",
        "Operating Hours": 450,
        "Downtime": 40,
        "Energy Consumption": 2200,
        "Units Produced": 9000,
        "Maintenance Cost": 22000
    },
    {
        "Machine ID": 103,
        "Plant Name": "Plant A",
        "Operating Hours": 600,
        "Downtime": 30,
        "Energy Consumption": 2800,
        "Units Produced": 15000,
        "Maintenance Cost": 18000
    },
    {
        "Machine ID": 104,
        "Plant Name": "Plant C",
        "Operating Hours": 400,
        "Downtime": 50,
        "Energy Consumption": 2000,
        "Units Produced": 7000,
        "Maintenance Cost": 25000
    }
]

print("=" * 100)
print("INDUSTRIAL IoT MACHINE PERFORMANCE MONITORING SYSTEM")
print("=" * 100)

# 1. Calculate Machine Efficiency
for m in machines:
    m["Efficiency"] = round(
        m["Units Produced"] /
        (m["Operating Hours"] - m["Downtime"]), 2
    )

# 2. Calculate Production Cost Per Unit
for m in machines:
    m["Cost Per Unit"] = round(
        m["Maintenance Cost"] /
        m["Units Produced"], 2
    )

# Display Machine Details
print("\nMachine Details")
print("-" * 110)
print(f'{"ID":<8}{"Plant":<12}{"Efficiency":<15}{"Cost/Unit":<15}{"Maintenance":<15}')
print("-" * 110)

for m in machines:
    print(f'{m["Machine ID"]:<8}'
          f'{m["Plant Name"]:<12}'
          f'{m["Efficiency"]:<15}'
          f'{m["Cost Per Unit"]:<15}'
          f'{m["Maintenance Cost"]:<15}')

print("-" * 110)

# 3. Identify Inefficient Machines
print("\n3. Inefficient Machines (Efficiency < 22)")

found = False
for m in machines:
    if m["Efficiency"] < 22:
        found = True
        print(m["Machine ID"], "-", m["Efficiency"])

if not found:
    print("No Inefficient Machines")

# 4. Machine with Highest Maintenance Cost
highest = max(machines, key=lambda x: x["Maintenance Cost"])

print("\n4. Highest Maintenance Cost")
print("Machine ID :", highest["Machine ID"])
print("Cost       :", highest["Maintenance Cost"])

# 5. Plant-wise Efficiency
print("\n5. Plant-wise Average Efficiency")

plant = {}

for m in machines:
    if m["Plant Name"] not in plant:
        plant[m["Plant Name"]] = []

    plant[m["Plant Name"]].append(m["Efficiency"])

print("-" * 35)
print(f'{"Plant":<15}{"Avg Efficiency":<15}')
print("-" * 35)

for p in plant:
    avg = sum(plant[p]) / len(plant[p])
    print(f'{p:<15}{round(avg,2):<15}')

print("-" * 35)

# 6. Preventive Maintenance
print("\n6. Machines Requiring Preventive Maintenance")

for m in machines:
    if m["Maintenance Cost"] > 20000:
        print("Machine", m["Machine ID"])

# 7. Sort Machines by Efficiency
machines.sort(key=lambda x: x["Efficiency"], reverse=True)

print("\n7. Machines Sorted by Efficiency")

print("-" * 40)
print(f'{"Machine":<15}{"Efficiency":<15}')
print("-" * 40)

for m in machines:
    print(f'{m["Machine ID"]:<15}{m["Efficiency"]:<15}')

print("-" * 40)

# 8. Generate Maintenance Report
print("\n8. Maintenance Report")

report = []

for m in machines:
    line = (f'Machine {m["Machine ID"]} | '
            f'Plant: {m["Plant Name"]} | '
            f'Efficiency: {m["Efficiency"]} | '
            f'Maintenance Cost: {m["Maintenance Cost"]}')

    report.append(line)
    print(line)

# 9. Save Report
with open("maintenance_report.txt", "w") as file:
    for line in report:
        file.write(line + "\n")

print("\nReport Saved Successfully")

# 10. Read Report
print("\n10. Reading Maintenance Report")

with open("maintenance_report.txt", "r") as file:
    print(file.read())

print("=" * 100)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 100)