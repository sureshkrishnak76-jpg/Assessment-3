# University Research Grant Allocation System

faculty = [
    {
        "Faculty ID": 101,
        "Faculty Name": "Alice",
        "Department": "CSE",
        "Publications": 25,
        "H-index": 15,
        "Budget": 120000,
        "Collaboration Score": 90
    },
    {
        "Faculty ID": 102,
        "Faculty Name": "Bob",
        "Department": "ECE",
        "Publications": 18,
        "H-index": 12,
        "Budget": 95000,
        "Collaboration Score": 80
    },
    {
        "Faculty ID": 103,
        "Faculty Name": "Charlie",
        "Department": "MECH",
        "Publications": 30,
        "H-index": 18,
        "Budget": 150000,
        "Collaboration Score": 95
    },
    {
        "Faculty ID": 104,
        "Faculty Name": "David",
        "Department": "CSE",
        "Publications": 20,
        "H-index": 14,
        "Budget": 110000,
        "Collaboration Score": 85
    }
]

print("=" * 60)
print("UNIVERSITY RESEARCH GRANT ALLOCATION SYSTEM")
print("=" * 60)

# Task 1: Calculate Research Score
print("\n1. Research Scores")

for f in faculty:
    score = (
        0.4 * f["Publications"]
        + 0.3 * f["H-index"]
        + 0.3 * f["Collaboration Score"]
    )
    f["Research Score"] = round(score, 2)
    print(f'{f["Faculty Name"]} : {f["Research Score"]}')

# Task 2: Allocate Grants
print("\n2. Grant Allocation")

for f in faculty:
    if f["Research Score"] >= 40:
        f["Grant"] = "Approved"
    else:
        f["Grant"] = "Rejected"

    print(f'{f["Faculty Name"]} -> {f["Grant"]}')

# Task 3: Faculty receiving grants above $100000
print("\n3. Faculty Receiving Grants Above $100000")

for f in faculty:
    if f["Budget"] > 100000:
        print(f'{f["Faculty Name"]} - ${f["Budget"]}')

# Task 4: Department receiving maximum funding
print("\n4. Department Receiving Maximum Funding")

department_funding = {}

for f in faculty:
    dept = f["Department"]
    department_funding[dept] = department_funding.get(dept, 0) + f["Budget"]

max_department = max(department_funding, key=department_funding.get)

print("Department Wise Funding")

for dept, amount in department_funding.items():
    print(dept, ":", amount)

print("\nMaximum Funding Department:", max_department)

# Task 5: Rank Faculty Members
print("\n5. Faculty Ranking")

faculty.sort(key=lambda x: x["Research Score"], reverse=True)

for rank, f in enumerate(faculty, start=1):
    f["Rank"] = rank
    print(rank, "-", f["Faculty Name"], "-", f["Research Score"])

# Task 6: Average Research Score
print("\n6. Average Research Score")

average = sum(f["Research Score"] for f in faculty) / len(faculty)

print("Average Score =", round(average, 2))

# Task 7: Top Performer
print("\n7. Top Performer")

top = faculty[0]

print("Faculty :", top["Faculty Name"])
print("Score   :", top["Research Score"])

# Task 8: Save Rankings to File
print("\n8. Saving Rankings")

with open("rankings.txt", "w") as file:
    for f in faculty:
        file.write(
            f'Rank {f["Rank"]} - {f["Faculty Name"]} - {f["Research Score"]}\n'
        )

print("Rankings saved successfully.")

# Task 9: Read Rankings
print("\n9. Reading Rankings")

with open("rankings.txt", "r") as file:
    print(file.read())

# Task 10: Handle Invalid Budgets
print("\n10. Invalid Budget Checking")

for f in faculty:
    try:
        if f["Budget"] < 0:
            raise ValueError("Invalid Budget")

        print(f'{f["Faculty Name"]} : Budget is Valid')

    except ValueError:
        print(f'{f["Faculty Name"]} : Invalid Budget')

print("\nProgram Completed Successfully.")