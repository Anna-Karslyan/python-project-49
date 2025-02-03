    
import random
import prompt

def ask(name):
    number = random.randint(1,100)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    if number % 2 == 0:
        
        if answer == 'yes':
            print('Correct!')
            return True
        elif answer == 'no':
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            return False
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            return False
    else:
        if answer == 'no':
            print('Correct!')
            return True
        elif answer == 'yes':
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            return False
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            return False
def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while True: 
        if counter == 3:
            print(f'Congratulations, {name}!')
            break
        if ask(name):
            counter += 1
        else:
            counter = 0

if __name__ == "__main__":
    main()

    

    