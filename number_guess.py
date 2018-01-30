# This is a guess the number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
print("你好，请问你叫什么名字？")
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
print("你好，"+myName+"，我现在想好了一个1到20之间的数字。")
while guessesTaken < 6:
    print('Take a guess.') # There are four spaces in front of print.
    print("猜一下")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.
        print("你猜的数字太小。")
    if guess > number:
        print('Your guess is too high.')
        print("你猜的数字太大。")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
    print('好样的， ' + myName + '！ 你猜了' + guessesTaken + '次就猜出来了！')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
    print('我想的数字是 ' + number)