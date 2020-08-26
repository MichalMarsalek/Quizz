from random import shuffle

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
class Question:
    """
    A record of a question and corresponding answers.
    
    Attributes:
        question: String question.
        answers: List of answers. Each answers is a pair of string answer and an int id.
        The correct answer is the one with an id 0.
    """
    def __init__(self, question, answers):
        """
        Args:
            question: String question.
            answers: List of string answers.
        """
        self.question = question
        self.answers = list(answers)
    
    def from_string(text):
        """
        Creates a Question object from text representation.
        
        Args:
            text: String representation
                - question then newline then the correct answer then newline separated other answers
        
        Returns:
            A Question object.
        """
        q, *a = text.splitlines()
        return Question(q, a)
    
    def shuffle(self):
        """
        Shuffles the answers corresponding to this question.
        """        
        shuffle(self.answers)
    
    @property
    def correct(self):
        """
        Canonical (uppercase sorted) answer to the question.
        
        Returns:
            String representing the correct answer indicating the correctness.
        """
        
        res = "".join(c for c,a in zip(ALPHA, self.answers) if a[0] == "+")
        if res == "":
            res = "-"
        return res
    
    def print(self):
        """
        Prints the question.
        
        Prints the question and then the answers in current (random) order."""
        print(self.question)
        for letter,a in zip(ALPHA, self.answers):
            print(f"{letter}) {a[1:]}")
            

class Quizz:
    """
    Object containing the complete quizz.
    
    Attributes:
        questions: List of Questions.
    """
    
    def __init__(self, questions):
        self.questions = questions
    
    def from_string(text):
        """
        Creates a Quizz object from a text representation.
        
        Args:
            text: String representation
                - Double newline separated text representations of Questions.
        
        Returns:
            Quizz object.
        """
        return Quizz([Question.from_string(q) for q in text.split("\n\n")])
    
    def from_file(path):
        """
        Creates a Quizz object from a text representation in a file.
        
        Args:
            path: String path to the file.
        
        Returns:
            Quizz object.
        """
        with open(path, encoding='utf-8') as f:
            data = "\n".join(f.read().splitlines())
        return Quizz.from_string(data)
    
    def shuffle(self):
        """
        Shuffles the order of questions and answers within each question.
        """
        
        shuffle(self.questions)
        for q in self.questions:
            q.shuffle()
    
    def run(self):
        """
        Runs the quizz.
        """
        
        questions = self.questions
        points = 0
        total = len(questions)
        for i in range(len(questions)):
            print(f"Question {i+1}/{len(questions)}:")
            questions[i].print()
            inp = "".join(sorted(input().upper()))
            if inp == "":
                inp = "-"
            if inp == questions[i].correct:
                points += 1
                print("Correct!")
            else:
                print(f"Incorrect! Correct answer is {questions[i].correct}.")
            print()
        print(f"Quizz is over - your score is {points}/{total}.")