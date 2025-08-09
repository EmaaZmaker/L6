class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+"("+ self.meaning+")"
flash=[]
print("welcome people to the flashcards apllication!")
while True:
    word=input("enter the word you want to add in the flashcard")
    meaning=input("enter the meaning of your word")
    flash.append(flashcard(word,meaning))
    option=int(input("enter zero(0) to continue/add a flashcard and press one(1) if you want to end"))
    if (option):
        break
print("your flashcards are")
for i in flash:
    print(">",i)