#Name ERic Farrar
#Prog Purpose:This magic 8-Ball code uses a python Tuple since the
#user does not have the ability to change the 8_Ball answers,
#However, the program could have used a Python list instead of a tuple.
#NOTE: Tuples use parenthese; lists use square braces.

import random
answers_8_ball = ("As I see it, yes", "Ask again later",
                  "Better not to tell you now", "Cannot predict now"
                  "Concentrate and ask again,", "Dont count on it",
                  "It is certain", "Most Likely", "My reply is no", "My sources say no",
                  "Outlook Good", "Outlook not so good", "Reply hazy try again", "yes", "You may rely on it",
                  "without a doubt",)

def main():
    print("I am the MAGIC-8 and can answer any YES or NO question!")

    another_question = True
    while another_question:
        answer = random.choice(answers_8_ball )

        print("\nShake the MAGIC-8 BALL")
        print("...and now...")
        question = input ("\nWhat is your YES or NO question? ")
        print("The MAGIC-8 BALL says: " + answer)

        askAgain= input("\nWould you like to ask me another question (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain == "n":
              another_question = False

    print("\nCome back again when you have other important questions.")
    print("...Magic-8 Ball OUT.")
main()

                          
                  
