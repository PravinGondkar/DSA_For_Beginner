# 🌀 Python Tuples — Immutable Data Containers
# -------------------------------------------------------
# Tuples are similar to lists, but they cannot be changed (immutable).
# They are often used to store fixed data, like database records, coordinates, etc.

# -------------------------------------------------------
# 1️⃣ Creating Tuples
# -------------------------------------------------------

# Empty tuple
empty_tuple = ()

# Tuple with multiple data types
person = ("Pravin", 28, "Data Engineer")

# Tuple without parentheses (packing)
data = 10, 20, 30

print("Empty Tuple:", empty_tuple)
print("Person Tuple:", person)
print("Packed Tuple:", data)
print("Type of data:", type(data))

# -------------------------------------------------------
# 2️⃣ Accessing Tuple Elements
# -------------------------------------------------------

numbers = (10, 20, 30, 40, 50)
print("\nTuple:", numbers)
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Middle slice:", numbers[1:4])

# -------------------------------------------------------
# 3️⃣ Tuple Immutability
# -------------------------------------------------------
# Tuples cannot be modified after creation.

try:
    numbers[0] = 99
except TypeError as e:
    print("\n❌ Error (Tuples are immutable):", e)

# -------------------------------------------------------
# 4️⃣ Iterating Through a Tuple
# -------------------------------------------------------
print("\nIterating through tuple:")
for num in numbers:
    print(num, end=" ")

# -------------------------------------------------------
# 5️⃣ Tuple Unpacking
# -------------------------------------------------------
person = ("Alice", 25, "Analyst")
name, age, role = person
print("\n\nUnpacked Values → Name:", name, "| Age:", age, "| Role:", role)

# -------------------------------------------------------
# 6️⃣ Nested Tuples
# -------------------------------------------------------
nested = (("A", 1), ("B", 2), ("C", 3))
print("\nNested Tuple:", nested)
print("Access inner value:", nested[1][1])

# -------------------------------------------------------
# 7️⃣ Tuple Methods — count() & index()
# -------------------------------------------------------
nums = (1, 2, 3, 2, 2, 4)
print("\nCount of 2:", nums.count(2))
print("Index of 3:", nums.index(3))

# -------------------------------------------------------
# 8️⃣ Converting Between Tuples and Lists
# -------------------------------------------------------
list_data = [10, 20, 30]
tuple_data = tuple(list_data)

print("\nConverted to Tuple:", tuple_data)
print("Back to List:", list(tuple_data))

# -------------------------------------------------------
# 9️⃣ Tuple in Data Engineering Context
# -------------------------------------------------------
# Tuples are useful for storing fixed schema data, e.g., extracted database rows.

employee_record = ("E123", "John Doe", "Engineering", 85000)
print("\nEmployee Record (tuple):", employee_record)

# Unpack for structured access
emp_id, emp_name, dept, salary = employee_record
print(f"Employee {emp_name} from {dept} earns ₹{salary} annually.")

# -------------------------------------------------------
# 🔟 Tuple of Tuples — Representing Tabular Data
# -------------------------------------------------------
records = (
    ("ID", "Name", "Dept", "Salary"),
    ("E101", "Alice", "Finance", 70000),
    ("E102", "Bob", "IT", 90000),
    ("E103", "Carol", "HR", 65000)
)

print("\nCompany Records (tuple of tuples):")
for row in records:
    print(row)

# -------------------------------------------------------
# 💡 Why Tuples Are Important for Data Engineers
# -------------------------------------------------------
"""
✅ Tuples are immutable → safer for read-only data like configurations, schema, etc.
✅ Faster than lists (less memory overhead)
✅ Often used in:
    • Row data fetched from SQL queries (each record is a tuple)
    • Keys in dictionaries (since they’re hashable)
    • Fixed pipelines and parameter definitions
"""

# -------------------------------------------------------
# 🧠 Quick Recap
# -------------------------------------------------------
"""
Feature              | List              | Tuple
---------------------|------------------|-----------------
Mutability           | Mutable           | Immutable
Syntax               | [ ]               | ( )
Performance          | Slower            | Faster
Usage Example        | Temp data buffer  | Fixed config, schema
"""
