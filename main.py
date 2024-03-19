import re

stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
valid = True
if("^" not in stdform or "x10" not in stdform or "." not in stdform):
  valid = False
mantissa = stdform[0: stdform.index("x10^")] 
exponent = stdform[stdform.index("x10^") + 4:]

if(exponent.count(".") != 0 or mantissa.count(".") > 1 or mantissa.count("-") > 1 or len(mantissa.lstrip("-")) != 3):
  valid = False


if(valid):
 
  
  print(f"This number in E notation is {mantissa}E{exponent}.")
else:
  print("Error converting to scientific E notation.")