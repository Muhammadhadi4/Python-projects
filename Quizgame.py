questions = [
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "Capital of Pakistan?", "answer": "Islamabad"},
    {"question": "What is 5 x 3?", "answer": "15"},
]

score = 0

for q in questions:
    print(q["question"])
    user_answer = input("Your answer: ")
    
    if user_answer == q["answer"]:
        print("Correct! ✅")
        score = score + 1
    else:
        print("Wrong! ❌")

print("Your final score:", score, "/", len(questions))
