for i in range(1, 15+1):
    if i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    else:
        print(f'{i}')
