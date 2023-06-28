import sys

sum = 0
nsum = 0

for _ in range(20):
    subj, num, grade = sys.stdin.readline().split()

    if grade != "P":
        num = float(num)
        nsum += num
        if grade != "F":
            if grade == "A+":
                num *= 4.5
            elif grade == "A0":
                num *= 4
            elif grade == "B+":
                num *= 3.5
            elif grade == "B0":
                num *= 3
            elif grade == "C+":
                num *= 2.5
            elif grade == "C0":
                num *= 2
            elif grade == "D+":
                num *= 1.5
            elif grade == "D0":
                num *= 1
            
            sum += num

print(sum/nsum)

