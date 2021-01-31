# task 1

for i in range(5):
    for l in range(2):
        print('Blue')
    for i in range(32,35):
        print(i)

# task 2

sum = 0

number = int(input('Please input how many numbers you would like to enter:'))

for i in range(number):
    hehe = float(input('Enter a number: \n'))
    sum += hehe

print('The average of the numbers you entered was', sum / number)