import numpy as np

temperatures = np.array([20,21,22,23,24,25,26])


highest = np.max(temperatures)
lowest = np.min(temperatures)
average = np.mean(temperatures)

print("Highest temperature:", highest)
print("Lowest temperature:", lowest)
print("Average temperature:", average)
