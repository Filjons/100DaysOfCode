target = int(input("Gimme a number between 0 and 1000!"))

sum = 0

for n in range(0, target + 1, 2):
    sum += n

print(sum)