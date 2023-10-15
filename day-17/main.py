from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    data = Question(question['question'], question['correct_answer'])
    question_bank.append(data)


quiz_brain = QuizBrain(question_bank)

while quiz_brain.is_still_has_questions():
    quiz_brain.next_question()

print("you complete the quiz")
print(f"your final score {quiz_brain.score}")