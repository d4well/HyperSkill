import random

name = input("Enter your name:")
print(f"Hello, {name}")

input_options = input()

ALL_OPTIONS = ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge', \
               'wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock']

wins = {option: [ALL_OPTIONS[i] for i in \
        range(ALL_OPTIONS.index(option)-1, ALL_OPTIONS.index(option) - 8, -1)]\
        for option in ALL_OPTIONS}

if input_options:
    options = input_options.split(',')
else:
    options = ['scissors', 'rock', 'paper']


def rating():
    with open('rock_paper_rating.txt', 'r') as f:
        names = {name.strip('\n').split()[0]: int(name.strip('\n').split()[1]) for name in f.readlines()}
    return names


def set_value():
    if name not in names:
            names[name] = 0


print("Okay, let's start")           
names = rating()
set_value()

while True:
    flag1 = True
    while flag1:
        user_input = input()
        if user_input == '!exit':
            flag1 = False
        elif user_input == '!rating':
            flag1 = False
        elif user_input not in options:
            print('Invalid input')
            continue
        else:
            flag1 = False
    comp_choice = random.choice(options)
    
    if user_input == '!exit':
        print('Bye!')
        break
    elif user_input == '!rating':
        print(names[name])
        continue
    elif user_input == comp_choice:
        names[name] += 50
        print(f"There is a draw ({user_input})")
        continue
    elif user_input in wins[comp_choice]:
        print(f"Sorry, but the computer chose {comp_choice}")
        continue
    else:
        names[name] += 100
        print(f"Well done. The computer chose {comp_choice} and failed")
        continue
    
    
