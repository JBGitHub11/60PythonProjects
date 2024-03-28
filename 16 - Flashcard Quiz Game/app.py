import json
import random

def load_flashcards(file_path):
    with open(file_path, 'r') as file:
        flashcards = json.load(file)
    return flashcards

def play_quiz(flashcards):
    random.shuffle(flashcards)
    score = 0
    total_questions = len(flashcards)

    for flashcard in flashcards:
        question = flashcard['question']
        answer = flashcard['answer']

        user_answer = input(f"\nQuestion: {question}\nYour answer: ")

        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")

    print(f"\nQuiz completed! Your score: {score}/{total_questions}")

def main():
    file_path = 'flashcards.json'
    flashcards = load_flashcards(file_path)
    play_quiz(flashcards)

if __name__ == '__main__':
    main()