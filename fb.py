for i in range(1, 15+1):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(f'{i}')
