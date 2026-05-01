print("---- welcome to my quiz game ----")

game = input("Do you want to play the game? (yes/no): ").strip().lower()

if game != "yes":
    print("Game exited. Bye 👋")
    quit()


print("Welcome, let's play a game 😄")
score = 0

question = input("What does CPU stand for? ").lower()
if question == "central processing unit":
    print("Correct ✅")
    score += 4
else:
    print("Incorrect ❌")
    score -= 1

question = input("What does GPU stand for? ").lower()
if question == "graphics processing unit":
    print("Correct ✅")
    score += 4
else:
    print("Incorrect ❌")
    score -= 1

question = input("What does RAM stand for? ").lower()
if question == "random access memory":
    print("Correct ✅")
    score += 4
else:
    print("Incorrect ❌")
    score -= 1

question = input("What does ROM stand for? ").lower()
if question == "read only memory":
    print("Correct ✅")
    score += 4
else:
    print("Incorrect ❌")
    score -= 1

print("Your marks:", score)

if score > 2:
    print("You are intelligent bro 😎 (PASS)")
else:
    print("Padhai kar le bhai 📚 (FAIL)")