# ACT3_valid_mark_average.py - KSD TVET / Tshwane North
# Activity 3: Valid-mark average - Read until -1
# Author: NYANGAZA - 2026-10-22

total = 0
count = 0

while True:  # unknown repetitions -> while, not for (Bridge question)
    mark = int(input("Enter mark (0-100) or -1 to stop: ").strip())
    
    if mark == -1:
        break  # sentinel - stop reading
    
    if 0 <= mark <= 100:
        total += mark
        count += 1
    else:
        print(f"Reject {mark}")  # Accept only 0-100, reject others

if count == 0:
    print("No valid marks entered.")
else:
    average = total / count
    print(f"Average: {average:.2f}")