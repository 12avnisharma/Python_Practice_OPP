class QuizBrain:

    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        if ((self.question_number+1) > len(self.question_list)):
            return False
        else :
            return True

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f'Q.{self.question_number} : {self.current_question.text}? (Ture/False)')
        self.check_answer(user_input, self.current_question.answer)

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            print('You got it right')
            self.score +=1
        else:
            print("That is wrong")
        print(f"Correct answer is {correct_answer}")
        print(f"Your current score is {self.score}")
        