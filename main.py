from Quizz import Quizz

def main():
    """
    Runs the quizz over and over.
    """
    while True:
        quizz = Quizz.from_file("data.txt")
        quizz.shuffle()
        quizz.run()
        print("Restart? Y/N")
        if input() not in "yY":
            break

if __name__ == "__main__":
    main()