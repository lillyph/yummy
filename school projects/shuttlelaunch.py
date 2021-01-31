curTemp = float(input('What is the current tempurature in Fahrenheit?\n'))
timeSinceLastLightning = float(input('How many minutes have passed since the last lightning strike?\n'))
windSpeed = float(input('What is the current wind speed?\n'))

for i in range(1):
    if curTemp <= 32 or curTemp >= 100:
        print('\nfalse')
        break
    elif timeSinceLastLightning < 45:
        print('\nfalse')
        break
    elif windSpeed > 34:
        print('\nfalse')
    else:
        print('\ntrue')