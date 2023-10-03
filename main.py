questions = [
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript", "Php", 4
    ],
    [
        "What is the capital of France?", "London", "Berlin", "Paris", "Madrid", 3
    ],
    [
        "Which planet is known as the Red Planet?", "Mars", "Venus", "Jupiter", "Saturn", 1
    ],
    [
        "What is the largest mammal in the world?", "Elephant", "Giraffe", "Blue Whale", "Lion", 3
    ],
    [
        "Who wrote the play 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain",
        2
    ],
    [
        "What is the largest organ in the human body?", "Heart", "Brain", "Skin", "Lungs", 3
    ],
    [
        "Which gas do plants absorb from the atmosphere?", "Oxygen", "Carbon Dioxide", "Hydrogen", "Nitrogen", 2
    ],
    [
        "Which element has the chemical symbol 'H'?", "Helium", "Hydrogen", "Lithium", "Nitrogen", 2
    ],
    [
        "In which country did the Olympic Games originate?", "Greece", "Italy", "France", "USA", 1
    ],
    [
        "What is the smallest prime number?", "1", "2", "3", "0", 2
    ],
    [
        "Which famous scientist developed the theory of general relativity?", "Isaac Newton", "Albert Einstein",
        "Stephen Hawking", "Galileo Galilei", 2
    ],
    [
        "Which animal is known as the 'King of the Jungle'?", "Tiger", "Gorilla", "Lion", "Leopard", 3
    ],
    [
        "Who painted the Mona Lisa?", "Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", "Claude Monet", 3
    ],
    [
        "What is the chemical symbol for gold?", "Go", "Au", "Gd", "Ag", 2
    ],
    [
        "Which famous ship sank on its maiden voyage in 1912?", "Lusitania", "Queen Mary", "Titanic", "Andrea Doria", 3
    ]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000,
          10000000]
money = 0
for i in range(0, len(questions)):

    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]} ")
    print(question[0])
    print(f"a. {question[1]}          b. {question[2]} ")
    print(f"c. {question[3]}          d. {question[4]} ")
    reply = int(input("Enter your answer (1-4) or  0 to quit:\t"))

    # Correct answer and checkpoint

    if reply == question[-1]:
        if i == 14:
            print("\n******* 1 Crore *********** ")
            break
        if i == 4 or i == 9:
            money = levels[i]
            print(
                f"\nCongratulations, you have won Rs. {levels[i]} \n you have cleared the Checkpoint and you will definitely take Rs.{levels[i]} Home ")
        else:
            print(f"\nCorrect answer, you have won Rs. {levels[i]}")
            money = levels[i]

    # quit by contestant
    if reply == 0:
        break

    # wrong answer by contestent
    if reply != question[-1]:
        print(f"\nWrong Answer \nCorrect answer was {question[-1]} ")
        if (0 <= i and i < 4):
            money = 0
            break
        if (4 <= i and i < 9):
            money = 10000
            break
        if (9 < i and i < 14):
            money = 320000
            break

print(f"\nYou have won Rs.{money} \nThanks for playing this game with me ,Thankyou !")

