fibonacci = [0,1]
done = False
while done == False:
    repetitions = input('Repeat for - ')
    try:
        for times in range(int(repetitions)):
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
            print(fibonacci[-1]/fibonacci[-2])
        print(fibonacci)
        done = True
    except ValueError:
        print('Not an integer, try again.')