from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:

    new_obj = Question(item["question"], item["correct_answer"])
    question_bank.append(new_obj)


new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_questions:
    new_quiz.next_question()

print("Quiz complete")
print(f"Your final score was: {new_quiz.score} / {new_quiz.question_number}")
