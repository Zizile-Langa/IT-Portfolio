goal = 100000
current = 27000
monthly = 10000

remaining = goal - current
months = remaining / monthly

print("Savings Goal:", goal)
print("Current Savings:", current)
print("Remaining:", remaining)
print("Months Needed:", round(months, 1))
