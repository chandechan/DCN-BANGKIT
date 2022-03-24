def exam_grade(score):
	if score ==100:
		grade = "Top Score"
	elif score >59.99:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65))   # Should be Pass
print(exam_grade(55))   # Should be Fail
print(exam_grade(60))   # Should be Pass
print(exam_grade(95))   # Should be Pass
print(exam_grade(100))  # Should be Top Score
print(exam_grade(0))    # Should be Fail