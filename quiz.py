#python quiz game
questions=("How many elements are there in periodic table?",
           "Who discovered nucleus?",
           "Who is the father of Biology?",
           "Who is the father of Computer?")
answers=("C","A","B","A")
options=(("A.115","B.108","C.118","D.119"),
         ("A.Rutherford","B.Goldstein","C.Einstein","D.Newton"),
         ("A.Theophrastus","B.Aristotle","C.Charles Babbage","D.Issac Newton"),
         ("A.Charles Babbage","B.Newton","C.Aristotle","D.Mike Shinoda"))
guesses=[]
question_num=0
score=0
print("-----------Quiz-----------")
for question in questions:
    print(question_num+1,end=". ")
    print(question)
    for option in options[question_num]:
        print(option, end=" ")
        print()
    guess=input("Enter (A,B,C,D)").upper()
    guesses.append(guess)
    if guess== answers[question_num]:
        print("CORRECT!")
        score+=5
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    print("--------------------------")
    question_num+=1
print("--------------------------")
print("      Result     ")
print("--------------------------")
print("Guesses: ")
for guess in guesses:
    print(guess,end=" ")
print()

print("Answers:")
for answer in answers:
    print(answer, end=" ")
print()

score=int(score/20*100)
print(f"Your score is {score}%")
print("Thank you for taking the test!")
print("\n \n \n")
