import random

rate = 0

default_options = ['rock', 'paper', 'scissors']
name = input("Enter your name:")
print("Hello, {name}".format(name=name))

file = open('rating.txt', 'r')
item = list(filter(lambda line: name in line, file.readlines()))

if len(item) > 0:
    _, score = item[0].split(" ")
    rate = int(score)

file.close()

options = input()

if not options:
    options = default_options
else:
    options = options.split(',')
    print("Okay, let's start")


def get_beatable_list(player_input):

    player_index = options.index(player_input)

    beatable = []

    current_index = player_index
    count = 0
    limit = (len(options) - 1) // 2

    while True:

        if current_index > len(options) - 1:
            current_index = 0

        if count > limit:
            break

        beatable.append(options[current_index])

        current_index += 1
        count += 1

    beatable.pop(0)

    return beatable


while True:
    user_input = input()
    bot_input = random.choice(options)

    if user_input == '!exit':
        print("Bye!")
        break

    if user_input == '!rating':
        print("Your rating: {rate}".format(rate=rate))

    if user_input not in options:
        print("Invalid input")
        continue

    if user_input == bot_input:
        rate += 50
        print("There is a draw {option}".format(option=user_input))
        continue

    beatable = get_beatable_list(user_input)

    if bot_input not in beatable:
        rate += 100
        print("Well done. The computer chose {option} and failed".format(option=bot_input))
        continue
    else:
        print("Sorry, but the computer chose {option}".format(option=bot_input))
