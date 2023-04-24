from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(text = question['question'], answer = question['correct_answer'])
    question_bank.append(new_question)

#print(question_bank[0].answer)
quiz = QuizBrain(question_bank)

while (quiz.still_has_questions()):
    quiz.next_question()

print(f"Your final score is : {quiz.score}")