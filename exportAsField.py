def convert(filename,steps):
    steps = steps[::-1]

    with open(filename) as file:
        contents = file.read().split('\n')
        dimensions = contents[0].split('x')
        width, height = int(dimensions[0]), int(dimensions[1])
        initial_state = contents[1].split(' ')
        print(initial_state)

    field = initial_state

    with open('result.txt', 'a') as file:
        print('Initial')
        print(' '.join(map(str, field)) + "\n")
        file.write(' '.join(map(str, field)) + "\n")

        for step in steps:
            for row in range(0,len(field)):
                index = field.index('0')
                match step:
                    case 'Right;':
                        if index + 1 < len(field):
                            old = field[index+1]
                            field[index+1] = '0'
                            field[index] = old
                            print('Right')
                            print(' '.join(map(str, field)) + "\n")
                            file.write(' '.join(map(str, field)) + "\n")
                            break
                        else:   
                            print("FAIL RIGHT")
                    case 'Left;':
                        if index - 1 >= 0:
                            old = field[index-1]
                            field[index-1] = '0'
                            field[index] = old
                            print('Left')
                            file.write(' '.join(map(str, field)) + "\n")
                            print(' '.join(map(str, field)) + "\n")
                            break
                        else:
                            print("FAIL LEFT")
                    case 'Up;':
                        if index - width >= 0:
                            old = field[index - width]
                            field[index - width] = '0'
                            field[index] = old
                            print('Up')
                            file.write(' '.join(map(str, field)) + "\n")
                            print(' '.join(map(str, field)) + "\n")
                            break
                        else:
                            print("FAIL UP")
                    case  'Down;':
                        if index + width < len(field):
                            old = field[index + width]
                            field[index + width] = '0'
                            field[index] = old
                            print('Down')
                            file.write(' '.join(map(str, field)) + "\n")
                            print(' '.join(map(str, field)) + "\n")
                            break
                        else:
                            print("FAIL DOWN")
                    case _:
                        print("FAIL ALL")

        file.write(str(steps) + "\n")

