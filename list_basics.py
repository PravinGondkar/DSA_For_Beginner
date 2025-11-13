# 🧾 Python Lists — Basics for Data Engineers

Lists are one of the most versatile data structures in Python.  
They’re widely used for data extraction, cleaning, and transformation in ETL pipelines.

In this notebook, we’ll explore:
- Common list operations (`max`, `min`, `sum`, `count`)
- Reversing lists (and common mistakes)
- Membership checks
- Real-world relevance for data engineers
🌀 Reversing Lists — Common Mistake & Correct Approach
📘 Code Cell
python
Copy code
# 🌀 Reversing Lists — Common Mistake & Correct Approach
# -------------------------------------------------------
# Many beginners confuse list.reverse with slicing [::-1].
# Let's understand the difference step by step.

num = [1, 2, 3, 4]

# ❌ Incorrect: assigning the method itself, not calling it
rev1 = num.reverse  # this only stores the function reference, doesn't execute it

# ✅ Correct: slicing method (creates a new reversed list)
rev2 = num[::-1]

print("Result of slicing [::-1]:", rev2)
print("Result of rev1:", rev1)  # Notice it's a method reference, not the reversed list
🧾 Output
sql
Copy code
Result of slicing [::-1]: [4, 3, 2, 1]
Result of rev1: <built-in method reverse of list object at 0x0000020F3A6B6C80>
✅ Correct Usage of reverse()
📘 Code Cell
python
Copy code
# Method 1 — reverse() modifies the list in place
num_copy = [1, 2, 3, 4]
num_copy.reverse()
print("Using reverse():", num_copy)

# Method 2 — slicing creates a new reversed list
num = [1, 2, 3, 4]
rev2 = num[::-1]
print("Using slicing:", rev2)
🧾 Output
pgsql
Copy code
Using reverse(): [4, 3, 2, 1]
Using slicing: [4, 3, 2, 1]
🧠 Key Takeaways
markdown
Copy code
| Method | Action | Returns | Mutates Original? |
|--------|---------|----------|-------------------|
| `list.reverse()` | Reverses *in place* | `None` | ✅ Yes |
| `list[::-1]` | Returns a *new* reversed list | List | ❌ No |

💬 **Real-World Tip:**
When writing ETL pipelines, prefer slicing (`[::-1]`) if you want to keep the original dataset unchanged.  
Use `.reverse()` only when memory optimization matters and you don’t need the old order anymore.
🧩 Basic List Operations
📘 Code Cell
python
Copy code
# 🧩 Basic List Operations
# These are the most commonly used operations in data pipelines to validate or summarize lists of values.

# -----------------------------------------------------
# 1️⃣ Find Maximum and Minimum elements
# -----------------------------------------------------
numbers = [4, 2, 9, 7, 5]
maximum = max(numbers)
minimum = min(numbers)

print("Input:", numbers)
print("Maximum =", maximum)
print("Minimum =", minimum)

# -----------------------------------------------------
# 2️⃣ Find Sum and Average of elements
# -----------------------------------------------------
numbers = [10, 20, 30, 40]
total_sum = sum(numbers)
average = total_sum / len(numbers)

print("\nInput:", numbers)
print("Sum =", total_sum)
print("Average =", average)

# -----------------------------------------------------
# 3️⃣ Check if an element exists in the list
# -----------------------------------------------------
num = 5
numbers = [1, 2, 3, 4, 5]
exists = num in numbers

print("\nInput list:", numbers)
print("Check if", num, "exists:", exists)

# -----------------------------------------------------
# 4️⃣ Count occurrences of an element
# -----------------------------------------------------
numbers = [1, 2, 3, 2, 2, 4]
element = 2
count = numbers.count(element)

print("\nInput list:", numbers)
print("Element to count:", element)
print("Occurrences =", count)
🧾 Example Output
mathematica
Copy code
Input: [4, 2, 9, 7, 5]
Maximum = 9
Minimum = 2

Input: [10, 20, 30, 40]
Sum = 100
Average = 25.0

Input list: [1, 2, 3, 4, 5]
Check if 5 exists: True

Input list: [1, 2, 3, 2, 2, 4]
Element to count: 2
Occurrences = 3
🧠 Why This Matters for Data Engineers
markdown
Copy code
These operations are heavily used when:

- ✅ Cleaning numeric data (`min`, `max`, `sum`)
- ✅ Validating extracted datasets (`in` checks)
- ✅ Counting frequency of elements for deduplication or aggregation

For example, you may calculate the maximum transaction amount or count how many times a value appears bef