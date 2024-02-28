import random

class Question(): 
    def __init__(self, size = 7):
        super().__init__()
        self.size = size
        self.questions = []
        self.set_questions(size)
        
    def set_questions(self, size):
        # sample questions
        all_questions = [
            {
                "question": "Which of the following is NOT a programming language?",
                "A": "Python",
                "B": "Java",
                "C": "HTML",
                "D": "Ruby",
                "correct_answer": "C"
            },
            {
                "question": "What does RAM stand for?",
                "A": "Random Access Memory",
                "B": "Read-Only Memory",
                "C": "Remote Access Management",
                "D": "Real-time Automated Monitoring",
                "correct_answer": "A"
            },
            {
                "question": "What is the purpose of an operating system?",
                "A": "To provide power to the computer",
                "B": "To manage hardware and software resources",
                "C": "To process data for output",
                "D": "To protect against viruses",
                "correct_answer": "B"
            },
            {
                "question": "What is the output of the following code snippet in Python: print(2 + '3')?",
                "A": "5",
                "B": "23",
                "C": "Error",
                "D": "32",
                "correct_answer": "C"
            },
            {
                "question": "What is the process of finding errors and fixing them within a program called?",
                "A": "Debugging",
                "B": "Compiling",
                "C": "Interpreting",
                "D": "Executing",
                "correct_answer": "A"
            },
            {
                "question": "What data structure uses Last In, First Out (LIFO) ordering?",
                "A": "Queue",
                "B": "Stack",
                "C": "Tree",
                "D": "Heap",
                "correct_answer": "B"
            },
            {
                "question": "Which sorting algorithm has the worst time complexity in the average case?",
                "A": "Bubble Sort",
                "B": "Merge Sort",
                "C": "Quick Sort",
                "D": "Insertion Sort",
                "correct_answer": "A"
            },
            {
                "question": "What does CPU stand for?",
                "A": "Central Processing Unit",
                "B": "Computer Processing Unit",
                "C": "Central Processor Unit",
                "D": "Computer Processor Unit",
                "correct_answer": "A"
            },
            {
                "question": "What is the binary representation of the decimal number 10?",
                "A": "1010",
                "B": "1001",
                "C": "1110",
                "D": "1100",
                "correct_answer": "A"
            },
            {
                "question": "What does RAM stand for in computing?",
                "A": "Random Access Memory",
                "B": "Read Access Memory",
                "C": "Running Application Memory",
                "D": "Rapid Access Memory",
                "correct_answer": "A"
            }
        ]

        self.questions = random.sample(all_questions, size)
    
    def get_questions(self):
        return self.questions