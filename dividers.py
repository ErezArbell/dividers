#!/usr/bin/python3

# Find the number with the most dividers up to 1000

numbers_up_to = 1000

dividers = {}

def num_of_dividers(n):
  count = 0
  for i in range(1, n+1, 1):
    if n % i == 0:
      count = count + 1
  return count

for number in range(1, numbers_up_to + 1, 1):
  num_divs = num_of_dividers(number)
  # print(f"{number}: {num_divs}")
  dividers[number] = num_divs

max = 0
index_max = 1
for index, value in dividers.items():
  if value > max:
    max = value
    index_max = index

print(f"The number {index_max} has the max of {max} dividers")
