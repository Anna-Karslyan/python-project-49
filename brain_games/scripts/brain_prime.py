import random
import prompt 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_answers_count = 0  

    while True:
        number = random.randint(1, 100) 
        correct_answer = "yes" if is_prime(number) else "no"
        
        print(f"Question: {number}")
        user_answer = prompt.string('Your answer: ')
        
        if user_answer == correct_answer:
            correct_answers_count += 1
            print("Correct!")
            if correct_answers_count == 3:
                print(f'Congratulations, {name}!')
                correct_answers_count = 0  
                break
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n Let's try again, {name}!")
            correct_answers_count = 0  
            
if __name__ == "__main__":
    main()
    