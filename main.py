#Project goal: to make a grade checker that takes in a list of mcq grades
#and it corrects them according to a preset list of correct answers
#next goal: make a class for students, and give them a characteristic called grade
#and they can use a method to get their quizzes graded
class Student:
    def __init__(self, name):
        self.name = name
        self.answers = ""
        self.grade = 0
    #method to assign answers to a quiz
    def assign_student_answers(self, answers):
        #answers needs to be a string
        self.answers = answers
    #method to grade the quiz
    def grade_quiz(self, correct):
        student_answers = []
        correct_list = []
        for i in range(len(self.answers)):
            student_answers.append(self.answers[i])
            correct_list.append(correct[i])
        num_correct = 0
        num_wrong = 0
        wrong_index = []

        if len(student_answers) != len(correct_list):
            print("the number of answers does not match the number of correct answers")
        else:
            for i in range(len(student_answers)):
                if student_answers[i] == correct_list[i]:
                    num_correct +=1
                else:
                    num_wrong +=1
                    wrong_index.append(i)
            self.grade = num_correct
            print("----- \nnumber of correct answers: " + str(num_correct))
            print("number of wrong answers: " + str(num_wrong)+"\n-----")
        for i in wrong_index:
            print("question #" + str(i+1))
            print("your answer:" + student_answers[i] + " correct answer:" +  correct_list[i])
            print("-----")
    #add a method to get a grade to the student

testStudent = Student("DING")
testStudent.assign_student_answers("abcdabcd")
testStudent.grade_quiz("abcdabcc")