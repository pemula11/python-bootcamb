class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):

        question = self.question_list[self.question_number]
        self.question_number += 1

        choice = input(f'Q{self.question_number}: {question.text} (True/False)')
        self.check_answer(choice, question.answer)

    def is_still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("yak betul")
            self.score += 1
            print(f"skor mu {self.score}/{self.question_number}")
        else:
            print("salah")
        print(f"jawabannya adalah {correct_answer}")