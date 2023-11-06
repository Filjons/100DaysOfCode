student_scores = ["78", "65", "89", "86", "55", "91", "64", "89"]
heighest_score = 0
score = 0
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    score = student_scores[n]
    if heighest_score < score:
        heighest_score = score

print(heighest_score)