student_heights = ["156", "178", "165", "171", "187"]
sum_heights = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum_heights += student_heights[n]

print(sum_heights/len(student_heights))

