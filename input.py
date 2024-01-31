student_name = str(input("What is your name?\n"))
coursework_mark = int(input("What is your coursework mark?\n"))
exam_score = int(input("What is the exam score?\n"))

exam_score_out_70 = (exam_score/100) * 70

print(f"Your exam score is \n{exam_score_out_70}")

final_score = float(exam_score_out_70) + coursework_mark

print(f"Your final score is \n{final_score}")

