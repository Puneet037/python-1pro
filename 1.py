import numpy as np

marks = np.array([[70, 76, 80],
                  [65, 85, 90],
                  [60, 70, 75]])

print("Original 3x3 matrix:")
print(marks)

reshaped = marks.reshape(1, 9)
print("\nReshaped Matrix (1x9):")
print(reshaped)

print("\nMarks of 1st student:")
print(marks[:, 0])

print("\nFirst two subjects:")
print(marks[0:2])

bonus_marks = marks.copy()
bonus_marks[0] = bonus_marks[0] * 2

print("\nAfter Bonus applied:")
print(bonus_marks)


# Element-wise multiplication
a = np.array([2, 4, 6])
b = np.array([1, 3, 5])

result = a * b

print("\nElement-wise multiplication result:")
print(result)