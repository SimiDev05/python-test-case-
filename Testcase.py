# print("hello guys")
# greetings = "Hello what's up"
# Name = input("please enter your name")
# print("you are welcome" + ' ' + Name)
# Age = input("how old are you")
# print("please confirm your age")
# splitstring = "if you are sure type yes \nif not type no"
# print(splitstring)
# print("the pet shop owner said \"he's resting\"")
# Asplitstring = "this is another split string but\.its not very long"
# print(Asplitstring)
# name = 'tim'
# age = 24
# print(name + str(age))

# parrot = "wonderland"
# print(parrot)
# print(parrot[3])    #call bracket ,start count from zero
# print(parrot[-3])
# print(parrot[0:3])
# print(parrot[-5:-2])
# print(parrot[0:8:2])
# number = "1, 2, 3, 4, 5, 6,"
# print(number[0::3])
#
# print("he's " "probably "  "pining")
# print("he's probably pining")
# print("hello " * 5)
# print("land" in parrot)

# print('there are 31 days in jan feb nov dec')
# jane = 'jan'
# faith = 'feb'
# _1st = 'mar'
# no = 31
# print('there are' + ' ' + str(no) + ' ' + 'days in' + ' ' + jane + ' ' + faith + ' ' + _1st)
# print('there are {0} days in {1}, {2}, {3}' .format(no, jane, faith, _1st))
# print('my age is {0} years and {1}' .format(24, 6))
# for i in range(1, 12):
#     print('No. {0:2} squared is {1:4} and cubed is {2:2}' .format(i, i**2, i**3))
# print(' Pi is aprox {0} and area is {1}' .format(22/7, 22*7))

# programflow

# for i in range(1, 5):
#     print('{0} is equals {1}' .format(i, i/2))
#     print('calc. complete')
#     print('please try again')
#
# name = str(input('hello \nplease enter your name: '))
# print('nice to meet you {0}' .format(name))
# age = int(input('how old are you {0}: ' .format(name)))
# print('{0} you just said you are {1} years old' .format(name, age))
#
# if age >= 18:
#     print('{0} your are old enough to enter this site' .format(name))
#     print('WELCOME')
# else:
#     print('{0} please come back in {1} years time' .format(name, 18-age))

print('please guess a number')
guess = int(input())
if guess < 5:
    print('please guess higher')
    int(input())
    if guess == 5:
        print('Correct')
    else:
        print('Wrong')
elif guess > 5:
        print('please guess lower')
        int(input())
        if guess == 5:
            print('Correct')
        else:
            print('Wrong')
else:
    print('you are smart you guessed right the first time')



