import time

USER_CREDENTIALS = {"naveen": "1234"}
quiz = {
    "What is the capital of India?": "c",
    "Which language is used for web apps?": "b",
    "What does CPU stand for?": "a",
    "Which is not a programming language?": "d"
}

options = [
    ["a) Mumbai", "b) Kolkata", "c) New Delhi", "d) Chennai"],
    ["a) Python", "b) JavaScript", "c) HTML", "d) SQL"],
    ["a) Central Processing Unit", "b) Control Program Unit", "c) Computer Processing Unit", "d) Central Programming Unit"],
    ["a) Python", "b) Java", "c) Ruby", "d) HTML"]
]

def login():
    print("Login")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        print("\nLogin Successful!\n")
        return True
    else:
        print("Invalid credentials. Try again.")
        return False

def take_exam():
    print("Starting Online Exam\n")
    score = 0
    i = 0

    for question, correct_ans in quiz.items():
        print(f"\nQ{i+1}: {question}")
        for option in options[i]:
            print(option)
        answer = input("Your answer (a/b/c/d): ").lower()

        if answer == correct_ans:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")

        i += 1
        time.sleep(1)

    print(f"\nExam Completed! Your Score: {score}/{len(quiz)}")

def main():
    print("=== Online Examination System ===")
    print("This project is developed by Naveen Thummala\n")

    if login():
        take_exam()
    else:
        print("Exiting...")

if __name__ == "__main__":
    main()
