while True:
    try:
        tables = int(input('How many multiplication tables you would like: '))
        if tables <= 0:
            print('Number must be greater than 0.')
        else:
            break
    except ValueError:
        print('That is not a number! Try again.')
        
while True:
    try:
        until = int(input('Until what number should each table go to (e.g 10 would end in x 10): '))
        if until <= 0:
            print('Number must be greater than 0.')
        else:
            break
    except ValueError:
        print('That is not a number! Try again.')

left = 1
right = 0
for x in range (1, tables + 1):
    for i in range(1, until + 1):
        right = i
        ans = right * left
        print(f'{left} x {right} = {ans}')
        
    print('-' * 3)
    left += 1