#for reading the test and anking questions
file = open("TestQuestions.txt", "r")
score = 0
for i in range(4):
    for i in range(4):
        q1 = file.readline()
        print(q1)

    answer = input("Answer: ")
    correct = file.readline()[0]
    if answer == correct:
        print("Correct")
        score += 1
    else:
        print("Wrong, the answer was",correct)
print("\nTest over\nYour score was",(score/4)*100,"%")
