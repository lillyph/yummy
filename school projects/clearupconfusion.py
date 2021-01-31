#task 1

# curTemp = float(input('What is the current tempurature in Fahrenheit?\n'))
# timeSinceLastLightning = float(input('How many minutes have passed since the last lightning strike?\n'))
# precipIntensity = float(input('What is the intensity of rain/snow?\n'))

# for i in range(1):
#     if curTemp < 32 or curTemp > 100:
#         print('\nfalse')
#         break
#     elif timeSinceLastLightning <= 45:
#         print('\nfalse')
#         break
#     elif precipIntensity > 5:
#         print('\nfalse')
#     else:
#         print('\ntrue')

#task 2
    
# a = input('enter three words seperated by spaces: ')
# b = a.find(' ')
# c = a.rfind(' ')
# print(a[c:],a[b+1:c], a[:b])

#task 3

# print('When prompted, enter in numbers you would like to be in the list one by one. When you are done, enter the number -998.\n')

# a = 0
# b = []
# sum = 0
# count = 0
# while a != -998:
#     a = int(input('Enter in a number:'))
#     b.append(a)

# for elem in b:
#     if elem // 2 != 0:
#         count += 1

# print('The number of odd numbers you entered was', count,'.')

#task 4

answer = 'y'

while answer == 'y':
    a = float(input('\nEnter a number: '))
    b = (input('\nEnter an operation (+, -, /, *, %, //, **): '))
    if b == '+':
        print('\nThe answer is', a + float(input('\nEnter your addend: ')))
    elif b == '-':
        print('\nThe answer is', a - float(input('\nEnter your subtrahend: ')))
    elif b == '/':
        print('\nThe answer is', a / float(input('\nEnter your dividend: ')))
    elif b == '//':
        print('\nThe answer is', a // float(input('\nEnter your dividend: ')))
    elif b == '*':
        print('\nThe answer is', a * float(input('\nEnter your multiplier: ')))
    elif b == '%':
        print('\nThe answer is', a % float(input('\nEnter your dividend: ')))
    elif b == '**':
        print('\nThe answer is', a ** float(input('\nEnter your power: ')))
    else:
        print('\nPlease enter a valid operation.')
        continue
    answer = input('\nWould you like to continue operations? Enter y for yes and no for no: ')

    