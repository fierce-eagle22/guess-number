import random
active = True
random_number = int(random.randint(1, 10))
attempt_count = 1
score = 0

game_start = input('Hello, do you wanna start the game? (Yes/No) ')
if game_start.lower() == 'yes':
    print('Great! Get ready... The game is starting!')
elif game_start.lower() == 'no':
    print('Okay, swing by when you wanna play!')
    active = False
else:
    print('You perhaps entered an invalid character.')
    active = False

while active and attempt_count <= 3:
    user_guess = int(input('Try to guess: '))
    if user_guess == 'score':
        print(score)
    if not active:
        print('The Game Is Over.')
    if user_guess == random_number:
        print('You guessed it right! Congratulations!')
        score += 10
        part_2 = input('Do you wish to continue? (Yes/No) ')
        if part_2.lower() == 'yes':
            active = True
            attempt_count = 1
        elif part_2.lower() == 'no':
            print(f'Sure, no means no. Your total score is {score}')
            active = False
    elif user_guess >= random_number:
        print(f'The number is smaller than {user_guess}')
        attempt_count += 1
        score += 2
    elif user_guess <= random_number:
        print(f'The number is bigger than {user_guess}')
        attempt_count += 1
        score += 2
    if attempt_count > 3:
        print('You have run out of your attempts. Checking your score...')
        if score >= 10:
            one_more = input(f'You have {score} points. Would you like to use 10 of them to continue? (Yes/No)')
            if one_more.lower() == 'yes':
                score -= 10
                active = True
                attempt_count = 1
            elif one_more.lower() == 'no':
                print(f'You decided to stop playing. Great job! Your total score is {score}.')
                active = False
        elif score < 10:
            print(f'Sorry, you do not have enough points to continue this game. Your total score is {score}.')
            active = False
