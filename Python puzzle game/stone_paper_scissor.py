#Stone Paper Scissor
import random

print('Who wants to play against the Super Computer? ')
player_name = input().title()

while True:
    print(player_name, ', how many rounds would you like to play? ')
    rounds = int(input())
    if rounds >= 1:
        break
    else:
        print('Play minimum 1 round')

players_score = 0
computers_score = 0

for i in range(1, rounds+1):
    print('Round', i, ':')
    print('1. Stone')
    print('2. Paper')
    print('3. Scissor')
    print('Make a choice')
    players_choice = int(input())
    computers_choice = random.choice(['Stone', 'Paper', 'Scissor'])

    if players_choice == 1: #Stone
        print('Players Choice: Stone')
        print('Super Computers Choice: ', computers_choice)
        if computers_choice == 'Stone':
            print('Tie')
        elif computers_choice == 'Paper':
            print('Paper wraps the Stone')
            print('Super Computer wins the round!')
            computers_score+=1
        elif computers_choice == 'Scissor':
            print('Stone breaks the Scissor')
            print(player_name, 'wins the round!')
            players_score+=1

    elif players_choice == 2: #Paper
        print('Players Choice: Paper')
        print('Super Computers Choice: ', computers_choice)
        if computers_choice == 'Stone':
            print('Paper wraps the Stone')
            print(player_name, 'wins the round!')
            players_score+=1
        elif computers_choice == 'Paper':
            print('Tie')
        elif computers_choice == 'Scissor':
            print('Scissor cuts the Paper')
            print('Super Computer wins the round!')
            computers_score+=1

    elif players_choice == 3:#Scissor
        print('Players Choice: Scissor')
        print('Super Computers Choice: ', computers_choice)
        if computers_choice == 'Stone':
            print('Stone breaks the Scissor')
            print('Super Computer wins the round!')
            computers_score += 1
        elif computers_choice == 'Paper':
            print('Scissor cuts the paper')
            print(player_name,'wins the round!')
            players_score+=1

        elif computers_choice == 'Scissor':
            print('Tie')
    else:
        print('Wrong Choice, round wasted!!!')

if players_score > computers_score:
    print(player_name, 'wins against the Super Computer!!!')
elif computers_score > players_score:
    print('Super Computer wins against', player_name, '!!!')
else:
    print('Game Draw!!!')
