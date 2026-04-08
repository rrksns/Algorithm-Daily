import sys

input = sys.stdin.readline

total = 0
sameAngle = set()
for _ in range(3):
    angle = int(input())
    sameAngle.add(angle)

    total += angle

if total == 180 and len(sameAngle) == 1:
    print("Equilateral")
elif total == 180 and len(sameAngle) == 2:
    print("Isosceles")
elif total == 180 and len(sameAngle) == 3:
    print("Scalene")
elif total != 180:
    print("Error")
