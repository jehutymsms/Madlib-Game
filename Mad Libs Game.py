#One of the best ideas to start experimenting you 
# hands-on python projects for students is working on Mad Libs Generator. 
# This is the perfect project for beginners who are just starting out with software development. 
# Primarily focused on strings, variables, and concatenation, 
# this project will teach you how to manipulate user-inputted data. The program design is such that it will ask users to enter a 
# series of inputs that will be considered as a Mad Lib. Mab lib is one of the python projects for beginners. 
#The input could be anything, an adjective, a noun, a pronoun, etc. Once all the inputs are entered, 
#the application will take the data and arrange the inputs into a story template form. Sound fun, right?


#Quarantine Mad Libs. 
#Let's have a little fun shall we?
#Copy and paste this either filling in the blanks yourself or allowing the predictive text to do it for you. If possible see if you can get a friend to do it with you. 
#After you post your completed Mad Lib, copy and paste this blank one in the comments so others can play too.
#Today is day (number) of quarantine. I am feeling so (emotion) that I (verb) into the (room in house) where I (verb) my (noun) to make myself feel (emotion). 
#After I did I (social media platform) (name) to tell them what I had done to try and save my (state of mind) during this confinement. 
#(name) couldn't believe I had (activity)! I said, "What else am I supposed to do?!" If this continues for (number) weeks, I just may (verb) from the (noun) of (place)!

import time

libs = ["number", "emotion", "verb", "room in a house", "verb", "noun", "emotion", 
"social media platform", "name", "state of mind", "name", "activity", "number", 
"verb", "noun", "place"]

def get_name():
    res =input("What is your name? ")
    return res

def question_game():
    res = input("Would you like to play a game? Y/N " )
    ye = ["Y", "yes", "y", "Yes"]
    ne = ["N", "No", "n", "no"]
    if res in ye:
        print("Awesome!! Lets do a Madlib!!!")
        time.sleep(1)
        return game1()
    if res in ne:
        print("I am sorry to hear that. It was a pleasure to meet you. Goodbye")
    else:
        print("I am sorry. I am only programmed to except the responses listed.")
        question_game()

def game1():
    ye = ["Y", "yes", "y", "Yes"]
    ne = ["N", "No", "n", "no"]
    respon = input("I will ask you for a number of words. Provide them to me as I ask for them. Ready?")
    if respon in ye:
        return madlib()
    if respon in ne:
        pass

def madlib():
  madlib = []
  for lib in libs:
    use = input("Please give me a " + lib + ". ")
    madlib.append(use)
    time.sleep(1)
  express = """
  Today is day {} of quarantine. I am feeling so {} that I {} into the {} where I {} my 
  {} to make myself feel {}. After I did I {} {} to tell them what I had done to try and 
  save my {} during this confinement. {} couldn't believe I had {}! I said, "What else 
  am I supposed to do?!" If this continues for {} weeks, I just may {} from the {} of {}!
    """
  express2 = express.format(*madlib)
  return print(express2)

def game_rules():
    print("Hello my name is Ada")

    name = get_name()

    print("Hello " + name + " it is a pleasure to meet you.")
    time.sleep(2)
    question_game()

game_rules()