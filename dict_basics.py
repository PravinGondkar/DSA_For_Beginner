"""
Nested Dictionary Practice Questions with Solutions
Upload this file to your GitHub profile.
"""

# 1. Access value in nested dict
# This example shows how to reach a value stored deep inside a nested dictionary structure.
# Useful when working with JSON-like data or API responses.
student = {
    "name": "Amit",
    "scores": {
        "math": 88,
        "science": 92
    }
}
science_score = student["scores"]["science"]
print("Science Score:", science_score)


# 2. Add new key inside nested dict
# Demonstrates how to insert a new inner key into an already existing nested dictionary.
company = {
    "emp1": {"name": "Raj", "salary": 50000}
}
company["emp1"]["department"] = "IT"
print("Updated Company:", company)


# 3. Update nested value
# Shows how to modify existing data deep inside a nested dictionary.
record = {
    101: {"name": "Sam", "age": 25}
}
record[101]["age"] = 26
print("Updated Age:", record)


# 4. Loop through nested dict
# This example iterates through each outer key and prints formatted inner values.
users = {
    1: {"name": "Amit", "city": "Pune"},
    2: {"name": "Rahul", "city": "Mumbai"},
}
for uid, info in users.items():
    print(f"User {uid} → {info['name']} from {info['city']}")


# 5. Total marks of each student
# Calculates total marks by accessing values inside each student's nested dictionary.
marks = {
    "A": {"math": 80, "sci": 90},
    "B": {"math": 70, "sci": 60}
}
for student, m in marks.items():
    total = m["math"] + m["sci"]
    print(f"Total marks of {student}: {total}")


# 6. Student with highest score
# Computes total scores for each student and finds who scored the highest.
totals = {k: v["math"] + v["sci"] for k, v in marks.items()}
highest = max(totals, key=totals.get)
print("Highest Scoring Student:", highest)


# 7. Flatten nested dict
# Converts a multi-level dictionary into a single flat dictionary for easier access.
data = {
    "emp": {
        "id": 101,
        "details": {"name": "Pravin", "city": "Mumbai"}
    }
}
flat = {
    "id": data["emp"]["id"],
    "name": data["emp"]["details"]["name"],
    "city": data["emp"]["details"]["city"]
}
print("Flattened Dict:", flat)


# 8. Count employees
# Counts total nested items across multiple departments inside a dictionary.
departments = {
    "IT": {"emp1": {}, "emp2": {}},
    "HR": {"emp1": {}, "emp2": {}, "emp3": {}}
}
count = sum(len(v) for v in departments.values())
print("Total Employees:", count)


# 9. Delete key inside nested dict
# Demonstrates how to safely remove a specific inner key from a nested structure.
product = {
    "mobile": {
        "brand": "Samsung",
        "price": 15000
    }
}
del product["mobile"]["price"]
print("Product After Deleting Price:", product)


# 10. Filter nested dict
# Filters entries in a nested dictionary based on a condition (city == Pune).
students = {
    "A": {"age": 20, "city": "Pune"},
    "B": {"age": 25, "city": "Mumbai"},
    "C": {"age": 30, "city": "Pune"}
}
pune_students = {k: v for k, v in students.items() if v["city"] == "Pune"}
print("Students from Pune:", pune_students)
