#Project goal: to make a grade checker that takes in a list of mcq grades
#and it corrects them according to a preset list of correct answers

student_answers = input ("enter the answers for the mcq questions (separate using spaces):")
correct_answers = input ("enter the correct answers (separate using spaces):" )
student_list = []
correct_list = []
for i in range(len(student_answers)):
    student_list.append(student_answers[i])
    correct_list.append(correct_answers[i])
num_correct = 0
num_wrong = 0

if len(student_list) != len(correct_list):
    #checks to make sure the lists are the same length
    print("the number of answers does not match the number of correct answers")
else:
    for i in range(len(student_list)):
        if student_list[i] == correct_list[i]:
            num_correct +=1
        else:
            num_wrong +=1
    print("number of correct answers: " + str(num_correct))
    print("number of wrong answers: " + str(num_wrong))
    