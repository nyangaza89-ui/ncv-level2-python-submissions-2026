# ACT4_cubes_total.py - Activity 4: Cubes and their total
# Author:NYANGAZA - 2026-10-22

n = int(input("Enter n: ").strip())
if n < 1:
    print("Rejection: n must be >= 1")
else:
    total = 0
    cubes = []
    for i in range(1, n+1):
        cube = i*i*i
        cubes.append(str(cube))
        total += cube
    print(f"Cubes: {', '.join(cubes)}")
    print(f"Total: {total}")