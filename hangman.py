#Hangman in Python
import random

words=("Echo","Drift","Velvet","Pulse","Crimson","Hollow","Frost",
       "Blaze","Whisper","Nova","Iron","Shade","Lush","Orbit","Flux",
       "Glint","Talon","Mist","Rift","Ashen","Ember","Shiver","Cinder",
       "Glimmer","Stone","Vortex","Sable","Thorn","Dusk","Aurora","Brine",
       "Pyre","Cloak","Haven","Shard","Briar","Onyx","Veil","Loom","Fable")
 #dictionary
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
            1: (" o ",
                "   ",
                "   "),
            2: (" o ",
                " | ",
                "   "),
            3: (" o ",
                "/| ",
                "   "),
            4: (" o ",
                "/|\\",
                "   "),
            5: (" o ",
                "/|\\",
                "/  "),
            6: (" o ",
                "/|\\",
                "/ \\")}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main(): 
    print("*********************************")
    print("*******Welcome to Hangman!*******")
    isCorrect=True
    wrong_guesses=0
    answer=random.choice(words).lower()
    hint=["_"]* len(answer)
    guessed_letter=set()
    while isCorrect:
        
        display_man(wrong_guesses)
        display_hint(hint)
        guess=input("Guess an alphabet: ").lower()
        
        if len(guess)!=1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letter:
            print(f"{guess} is already guessed")
            continue
        guessed_letter.add(guess)
        
        if guess in answer:
            for x in range(len(answer)):
                if guess==answer[x]:
                    hint[x]=guess
        else:
            wrong_guesses+=1

        if "_" not in hint:
            display_man(wrong_guesses)
            print("You won!")
            display_answer(answer)
            print("*********************************")
            print("*********************************")
            isCorrect=False

        elif wrong_guesses>=6:
            display_man(wrong_guesses)
            print("You lost! Try again")
            display_answer(answer)
            print("*********************************")
            print("*********************************")
            
            isCorrect=False
            
if __name__=='__main__':
    main()