"""
Python Quiz Game

Author: Danilo Vunza
Course: COSC 1436

Description:
A multiple-choice quiz game that tracks
user score and displays final results.
"""


def display_question(question_data):

    print("\n" + "=" * 50)

    print(question_data["question"])

    print("=" * 50)

    for option in question_data["options"]:

        print(option)

    print()


def get_valid_answer():

    while True:

        answer = input(
            "Enter your answer (A, B, C, D): "
        ).upper()

        if answer in ["A", "B", "C", "D"]:

            return answer

        print("Invalid choice. Try again.")


def display_results(score, total_questions):

    percentage = (
        score / total_questions
    ) * 100

    print("\n" + "=" * 50)

    print("QUIZ RESULTS")

    print("=" * 50)

    print(
        f"Correct Answers: {score}"
    )

    print(
        f"Total Questions: {total_questions}"
    )

    print(
        f"Score Percentage: {percentage:.2f}%"
    )

    if percentage >= 90:

        print("Performance: Excellent")

    elif percentage >= 75:

        print("Performance: Good")

    elif percentage >= 60:

        print("Performance: Fair")

    else:

        print("Performance: Needs Improvement")


def main():

    questions = [

        {
            "question":
            "What does CPU stand for?",

            "options":
            [
                "A. Central Processing Unit",
                "B. Computer Personal Unit",
                "C. Central Program Utility",
                "D. Control Processing Unit"
            ],

            "answer": "A"
        },

        {
            "question":
            "Which language is used in COSC 1436?",

            "options":
            [
                "A. Java",
                "B. C++",
                "C. Python",
                "D. JavaScript"
            ],

            "answer": "C"
        },

        {
            "question":
            "Which symbol is used for comments in Python?",

            "options":
            [
                "A. //",
                "B. #",
                "C. /*",
                "D. --"
            ],

            "answer": "B"
        },

        {
            "question":
            "What data type stores whole numbers?",

            "options":
            [
                "A. float",
                "B. string",
                "C. integer",
                "D. boolean"
            ],

            "answer": "C"
        },

        {
            "question":
            "Which loop repeats while a condition is true?",

            "options":
            [
                "A. for",
                "B. repeat",
                "C. while",
                "D. loop"
            ],

            "answer": "C"
        }

    ]

    score = 0

    print("=" * 50)
    print("PYTHON QUIZ GAME")
    print("=" * 50)

    for question in questions:

        display_question(question)

        user_answer = get_valid_answer()

        if user_answer == question["answer"]:

            print("Correct!")

            score += 1

        else:

            print(
                f"Incorrect. Correct answer: "
                f"{question['answer']}"
            )

    display_results(
        score,
        len(questions)
    )


main()
