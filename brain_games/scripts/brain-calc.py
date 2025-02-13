import random
import prompt
def ask(name):
    operators = ['+','-','*']
    a = random.randint(1,100)
    b = random.randint(1,100)
    c = random.choice(operators)
    exp = f'{a} {c} {b}'
    print(f'Question: {exp}')
    answer = prompt.string('Your answer: ')
    try:

        if answer == str(eval(exp)):
            print('Correct!')
            return True
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{eval(exp)}'.\n Let's try again, {name}!")
            return False
        
    except:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{eval(exp)}'.\n Let's try again, {name}!")
        return False

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
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

    

    