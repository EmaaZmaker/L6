import random
class fruit_quiz:
    def __init__(self):
        self.fruits={"apple":"red",
                     "watermelon":"green",
                     "orange":"orange",
                     "banana":"yellow"}
    def quiz(self):
        while True:
            fruit,color=random.choice(list(self.fruits.items()))
            user_input=print(f"what is the color of {fruit}?")
            if (user_input.lower()==color):
                print("Good guess!")
            else:
                print("oops, sorry, your wrong!")
            option=int(input("enter 0 to continue otherwise 1"))
            if option:
                break
ob1=fruit_quiz()
ob1.quiz()