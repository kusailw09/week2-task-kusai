import json

# Example content of quiz.json:
# [
#   {"q": "Capital of India?", "a": "Delhi"},
#   {"q": "2 + 2 = ?", "a": "4"},
#   {"q": "Color of sky?", "a": "Blue"}
# ]

with open("quiz.json", "r") as f:
    quiz = json.load(f)

score = 0
for item in quiz:
    print(item["q"])
    ans = input("Answer: ").strip()
    if ans.lower() == item["a"].lower():
        print(" Correct!\n")
        score += 1
    else:
        print(f" Wrong! Correct answer: {item['a']}\n")

print(f"Your Final Score: {score}/{len(quiz)}")