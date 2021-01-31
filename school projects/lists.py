b = []
sum = 0
count = 0
for i in range(10):
    a = int(input('Enter in a number:'))
    b.append(a)

for elem in b:
    count += 1
    sum += elem

print('The average of the the numbers you entered was', sum / count, '.')
    