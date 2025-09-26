import array  # Import the array module

# 1. Create an array named 'scores' that stores five test scores (integers).
scores = array.array('i', [85, 90, 88, 92, 87])

# 2. Print the third score in the array.
print(scores[2])
# Arrays use indexing just like lists.

# 3. Change the second score to a new value.
# Modify an element by accessing it through its index.
scores[1] = 95

# 4. Add a new score to the array.
# Use append() to add a new element.
scores.append(93)
# 5. Print the updated array.
# Should show: array('i', [85, 95, 88, 92, 87, 93])
print(array)
