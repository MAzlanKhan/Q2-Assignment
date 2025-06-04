*Output of a Program:* 

import math

def sqrt_num(num):
  """Returns the square root of a number."""
  if num < 0:
    return "Cannot calculate square root of a negative number."
  else:
    return math.sqrt(num)

number = float(input("Enter a number: "))
result = sqrt_num(number)
print(f"The square root of {number} is: {result}")