🌀 Reversing Lists — Common Mistake & Correct Approach
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


Output:

Result of slicing [::-1]: [4, 3, 2, 1]
Result of rev1: <built-in method reverse of list object at 0x0000020F3A6B6C80>

✅ Correct Usage of reverse()
# Method 1 — reverse() modifies the list in place
num_copy = [1, 2, 3, 4]
num_copy.reverse()
print("Using reverse():", num_copy)

# Method 2 — slicing creates a new reversed list
num = [1, 2, 3, 4]
rev2 = num[::-1]
print("Using slicing:", rev2)


Output:

Using reverse(): [4, 3, 2, 1]
Using slicing: [4, 3, 2, 1]

🧠 Key Takeaways
Method	Action	Returns	Mutates Original?
list.reverse()	Reverses in place	None	✅ Yes
list[::-1]	Returns a new reversed list	List	❌ No
💬 Real-World Tip:

When writing ETL pipelines, prefer slicing ([::-1]) if you want to keep the original dataset unchanged.
Use .reverse() only when memory optimization matters and you don’t need the old order anymore.