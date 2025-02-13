import random
import prompt

def prog():
    step = random.randint(2, 5)
    list_prog = [random.randint(1, 10)]
    for i in range(9):
        list_prog.append(list_prog[i] + step)

    rand_ind = random.randint(0, 9)
    num = list_prog[rand_ind] 
    list_prog[rand_ind] = '..'

    str_prog = ""
    for i in list_prog:
        str_prog = str_prog + " "+str(i)

    return str(num), str_prog



def ask(name):
    num, str_prog = prog()
    print(f'Question: {str_prog}')
    answer = prompt.string('Your answer: ')
    try:

        if answer == num:
            print('Correct!')
            return True
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{num}'.\n Let's try again, {name}!")
            return False
        
    except:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{num}'.\n Let's try again, {name}!")
        return False

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
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