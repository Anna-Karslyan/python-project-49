import random
import prompt

def gcd(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

def ask(name):
    a = random.randint(1,100)
    b = random.randint(1,100)
    nod = gcd(a, b)
    exp = f'{a} {b}'
    print(f'Question: {exp}')
    answer = prompt.string('Your answer: ')
    try:
        if answer == str(nod):
            print('Correct!')
            return True
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{nod}'.\n Let's try again, {name}!")
            return False
        
    except:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{nod}'.\n Let's try again, {name}!")
        return False
    
def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
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